#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ThreadNote 자동 배치 정밀 고도화 엔진 v3
- 배치 단위(12개씩)로 상세 콘텐츠 리모델링
- 이모지 클러터 제거 + 볼드체 + 줄바꿈 + 맞춤 댓글
- 카테고리 교정
- 토큰 소비 제로 (API 미호출)
- 진행 상황을 scratch/progress.json에 기록
"""

import json
import re
import os
import sys
import time

DB_PATH = "/Users/wang/Documents/threadnote/uploads/user_threads.json"
PROGRESS_PATH = "/Users/wang/Documents/threadnote/scratch/progress.json"
LOG_PATH = "/Users/wang/Documents/threadnote/scratch/refactor_log.txt"

# ─── 유틸 함수 ────────────────────────────────────────────────

def load_db():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def log(msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def load_progress():
    if os.path.exists(PROGRESS_PATH):
        with open(PROGRESS_PATH, "r") as f:
            return json.load(f)
    return {"last_completed": 251}

def save_progress(idx):
    with open(PROGRESS_PATH, "w") as f:
        json.dump({"last_completed": idx}, f)

# ─── 정제 함수 ─────────────────────────────────────────────────

def clean_emojis(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'\*?\*?[1-9]️⃣\*?\*?[\s]*', '', text)
    text = re.sub(r'\*?\*?🔟\*?\*?[\s]*', '', text)
    text = re.sub(r'^[ \t]*[📍⭕👉▶️➗▪️▫️■□◎◆◇●○][ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'([ \n])[📍⭕👉▶️➗▪️▫️■□][ \t]*', r'\1', text)
    return text.strip()

def clean_latex(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', text)
    text = text.replace('\\times', '×').replace('\\div', '÷')
    text = text.replace('\\pm', '±').replace('\\approx', '≈')
    text = text.replace('\\cdot', '·').replace('\\pi', 'π')
    text = text.replace('\\square', '□').replace('\\triangle', '△')
    text = text.replace('\\(', '').replace('\\)', '')
    text = re.sub(r'\$([^$\n]+)\$', r'\1', text)
    return text

def detect_subject(thread):
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    sc = str(thread.get("sub_category", ""))
    posts = " ".join(p.get("text", "") for p in thread.get("posts", [])[:1])
    combined = f"{ititle} {sc} {posts}"

    rules = [
        (["도덕", "콜버그", "피아제", "배려윤리", "인격교육", "덕교육", "하인츠"], ("moral", "도덕")),
        (["미술", "로웬펠드", "펠드만", "판화", "조형", "도식기", "라이하트", "DBAE"], ("art", "미술")),
        (["음악", "달크로즈", "코다이", "오르프", "고든", "장단", "오스티나토", "가창", "리듬음절"], ("music", "음악")),
        (["체육", "PAPS", "TGfU", "라반", "스포츠", "도전영역", "경쟁영역", "체력", "PSI"], ("pe", "체육")),
        (["실과", "식생활", "식품구성", "스마트팜", "수송기술", "발명", "SCAMPER", "친환경농업", "가정"], ("practical_arts", "실과")),
        (["영어", "CLT", "TBLT", "크라센", "스웨인", "PPP", "파닉스", "TPR", "형태초점"], ("english", "영어")),
        (["과학", "달의", "태양", "광합성", "5E", "POE", "순환학습", "귀추", "가설연역"], ("science", "과학")),
        (["사회", "민주주의", "다수결", "논쟁문제", "의사결정", "뱅크스", "지리", "역사", "헌법", "경제"], ("social", "사회")),
        (["총론", "학교자율시간", "핵심역량", "2022 개정", "깊이있는"], ("general", "총론")),
        (["국어", "읽기", "쓰기", "문학", "문법", "직소", "반응중심", "한글"], ("korean", "국어")),
        (["수학", "분수", "도형", "측정", "연산", "반힐레", "폴리아", "딘즈", "확률", "통계"], ("math", "수학")),
    ]
    for kws, cat in rules:
        if any(k in combined for k in kws):
            return cat
    # Title prefix
    for prefix, cat in [("국어", ("korean","국어")), ("수학", ("math","수학")), ("사회", ("social","사회")),
                        ("과학", ("science","과학")), ("도덕", ("moral","도덕")), ("체육", ("pe","체육")),
                        ("음악", ("music","음악")), ("미술", ("art","미술")), ("실과", ("practical_arts","실과")),
                        ("영어", ("english","영어")), ("통합", ("integrated","통합교과")), ("총론", ("general","총론"))]:
        if ititle.startswith(prefix):
            return cat
    return (thread.get("main_category", "general"), thread.get("category", "공통"))

def make_comments(topic):
    t = re.sub(r'[\(\)\[\]_\\/]', ' ', topic).strip()
    t = re.sub(r'\s+', ' ', t)
    return [
        {"author": "단권화_장인", "handle": "summary_master", "avatar": "📒", "persona_name": "단권화_장인",
         "text": f"'{t}' 핵심 개념의 공식 명칭과 조작적 정의를 한 세트로 묶어 단권화해두면 실전 인출 속도가 비약적으로 향상됩니다.",
         "content": f"'{t}' 핵심 개념의 공식 명칭과 조작적 정의를 한 세트로 묶어 단권화해두면 실전 인출 속도가 비약적으로 향상됩니다."},
        {"author": "기출분석_고수", "handle": "exam_expert", "avatar": "🔎", "persona_name": "기출분석_고수",
         "text": f"기출 패턴: '{t}'는 교사 발문과 학생 반응을 맥락으로 제시하고, 이론·모형·절차를 서술하는 형태로 빈출됩니다.",
         "content": f"기출 패턴: '{t}'는 교사 발문과 학생 반응을 맥락으로 제시하고, 이론·모형·절차를 서술하는 형태로 빈출됩니다."},
        {"author": "새벽공부_불꽃초시생", "handle": "fire_beginner", "avatar": "🔥", "persona_name": "새벽공부_불꽃초시생",
         "text": f"이 제재의 유사 개념과 헷갈리는 오개념을 짚어놓는 게 부분 감점 방어의 핵심이에요!",
         "content": f"이 제재의 유사 개념과 헷갈리는 오개념을 짚어놓는 게 부분 감점 방어의 핵심이에요!"},
        {"author": "답안지_채점관", "handle": "scorer_official", "avatar": "✍️", "persona_name": "답안지_채점관",
         "text": f"채점관 기준: '{t}' 문항은 교육과정 공식 학술 명칭과 지도 절차의 위계가 정확해야 만점을 부여합니다.",
         "content": f"채점관 기준: '{t}' 문항은 교육과정 공식 학술 명칭과 지도 절차의 위계가 정확해야 만점을 부여합니다."},
    ]

def needs_refactor(thread):
    """기존 2인 댓글 레거시 or 이모지 클러터 or 카테고리 오류"""
    cmts = thread.get("comments", [])
    if len(cmts) < 4:
        return True
    if cmts[0].get("author") in ["핵심힌터_멘토", "멘토", "칼채점_분석관"]:
        return True
    posts_str = " ".join(p.get("text","") for p in thread.get("posts",[]))
    if any(e in posts_str for e in ["1️⃣","2️⃣","📍","⭕"]):
        return True
    return False

def refactor_thread(thread):
    # 1. Category
    cat_id, cat_name = detect_subject(thread)
    thread["main_category"] = cat_id
    thread["category"] = cat_name

    # 2. Clean posts
    for p in thread.get("posts", []):
        t = p.get("text", "")
        t = clean_emojis(t)
        t = clean_latex(t)
        p["text"] = t

    # 3. Title
    if not thread.get("title"):
        insight = thread.get("source_insight", {})
        ititle = insight.get("title", "")
        sc = thread.get("sub_category", "")
        topic = ititle.split(">")[-1].strip() if ">" in ititle else (sc or ititle)
        thread["title"] = f"{cat_name}: {topic}"

    # 4. Comments
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    sc = str(thread.get("sub_category", ""))
    topic = ititle.split(">")[-1].strip() if ">" in ititle else (sc or ititle or "핵심 제재")
    topic = topic[:30]
    cmts = make_comments(topic)
    thread["comments"] = cmts
    thread["simulated_comments"] = cmts

    # 5. Tags
    banned = {"#10개년빈출","#칼채점키워드","#감점주의","#초등임용","#초등임용고시"}
    old_tags = [t for t in thread.get("tags",[]) if t not in banned]
    cat_tag = f"#{cat_name}"
    if cat_tag not in old_tags:
        old_tags.insert(0, cat_tag)
    thread["tags"] = old_tags[:8]

    return thread

# ─── 메인 루프 ─────────────────────────────────────────────────

def run_batch(start_idx, batch_size=24):
    db = load_db()
    total = len(db)
    end_idx = min(start_idx + batch_size, total)

    log(f"▶ Batch [{start_idx}~{end_idx-1}] 시작")

    count = 0
    for i in range(start_idx, end_idx):
        t = db[i]
        if needs_refactor(t):
            db[i] = refactor_thread(t)
            count += 1

    save_db(db)
    save_progress(end_idx - 1)
    log(f"✓ Batch [{start_idx}~{end_idx-1}] 완료. 수정: {count}개. DB 저장 완료.")
    return end_idx

if __name__ == "__main__":
    progress = load_progress()
    start = progress.get("last_completed", 251) + 1

    db = load_db()
    total = len(db)

    log(f"=== 자동 배치 엔진 시작 | 총 {total}개 | 시작 인덱스: {start} ===")

    BATCH_SIZE = 24
    idx = start
    while idx < total:
        idx = run_batch(idx, BATCH_SIZE)
        if idx >= total:
            break

    log(f"=== 전체 {total}개 스레드 리팩토링 완료! ===")
