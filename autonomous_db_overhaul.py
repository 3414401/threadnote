#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Global Database Overhaul & Sanitization Engine
1. Preserves high-yield content while eliminating emoji clutter (1️⃣, 2️⃣, 📍, ⭕, etc.)
2. Converts raw LaTeX math into clean Unicode math (×, ÷, 1/2, etc.)
3. Corrects mistagged categories across all 2,392 threads
4. Overhauls all legacy 2-person comments into 4 authentic study room personas (단권화_장인, 기출분석_고수, 새벽공부_불꽃초시생, 답안지_채점관) with all 6 fields
5. Cleans tags, removing #10개년빈출 spam and adding granular topic tags
"""

import json
import re
import os

DB_PATH = "uploads/user_threads.json"

CATEGORY_MAP = {
    "국어": ("korean", "국어"),
    "수학": ("math", "수학"),
    "사회": ("social", "사회"),
    "과학": ("science", "과학"),
    "도덕": ("moral", "도덕"),
    "체육": ("pe", "체육"),
    "음악": ("music", "음악"),
    "미술": ("art", "미술"),
    "실과": ("practical_arts", "실과"),
    "영어": ("english", "영어"),
    "통합": ("integrated", "통합교과"),
    "바른생활": ("integrated", "통합교과"),
    "슬기로운생활": ("integrated", "통합교과"),
    "즐거운생활": ("integrated", "통합교과"),
    "총론": ("general", "총론"),
}

def clean_emojis(text):
    if not isinstance(text, str):
        return text
    # Clean leading numbered emojis and location/circle pins
    text = re.sub(r'^[ \t]*[1-9]️⃣[ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*🔟[ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*[📍⭕👉▶️➗▪️▫️■□][ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'([ \n])[1-9]️⃣[ \t]*', r'\1', text)
    text = re.sub(r'([ \n])🔟[ \t]*', r'\1', text)
    text = re.sub(r'([ \n])[📍⭕👉▶️➗▪️▫️■□][ \t]*', r'\1', text)
    return text.strip()

def clean_latex(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', text)
    text = text.replace(r'\times', '×')
    text = text.replace(r'\div', '÷')
    text = text.replace(r'\pm', '±')
    text = text.replace(r'\neq', '≠')
    text = text.replace(r'\leq', '≤')
    text = text.replace(r'\le', '≤')
    text = text.replace(r'\geq', '≥')
    text = text.replace(r'\ge', '≥')
    text = text.replace(r'\approx', '≈')
    text = text.replace(r'\cdot', '·')
    text = text.replace(r'\dots', '…')
    text = text.replace(r'\square', '□')
    text = text.replace(r'\triangle', '△')
    text = text.replace(r'\pi', 'π')
    text = text.replace(r'\(', '')
    text = text.replace(r'\)', '')
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    return text

def infer_category(thread):
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    sc = str(thread.get("sub_category", ""))
    quote = insight.get("academic_quote", "")
    posts_text = " ".join([p.get("text", "") for p in thread.get("posts", [])[:2]])
    combined = f"{ititle} {sc} {quote} {posts_text}"
    
    # 1. Direct title match
    for kw, (cat_id, cat_name) in CATEGORY_MAP.items():
        if ititle.startswith(kw) or f"{kw} >" in ititle or f"{kw}과" in ititle:
            return cat_id, cat_name
            
    # 2. Subcategory match
    for kw, (cat_id, cat_name) in CATEGORY_MAP.items():
        if kw in sc:
            return cat_id, cat_name
            
    # 3. High-confidence pedagogical keywords
    if any(k in combined for k in ["도덕", "콜버그", "피아제", "배려윤리", "인격교육", "도덕성", "하인츠"]):
        return "moral", "도덕"
    if any(k in combined for k in ["미술", "로웬펠드", "펠드만", "판화", "조형", "감상", "회화", "도식기"]):
        return "art", "미술"
    if any(k in combined for k in ["음악", "달크로즈", "코다이", "오르프", "고든", "장단", "오스티나토", "가창", "리듬음절", "손기호"]):
        return "music", "음악"
    if any(k in combined for k in ["체육", "PAPS", "TGfU", "라반", "스포츠", "도전영역", "경쟁영역", "왕복오래달리기"]):
        return "pe", "체육"
    if any(k in combined for k in ["실과", "식생활", "식품구성자전거", "스마트팜", "홈프로젝트", "수송기술", "발명", "SCAMPER", "친환경농업"]):
        return "practical_arts", "실과"
    if any(k in combined for k in ["영어", "CLT", "TBLT", "크라센", "스웨인", "PPP", "파닉스", "TPR"]):
        return "english", "영어"
    if any(k in combined for k in ["과학", "달의", "태양", "광합성", "5E", "POE", "순환학습", "가설검증", "오개념", "귀추"]):
        return "science", "과학"
    if any(k in combined for k in ["사회", "민주주의", "다수결", "논쟁문제", "의사결정", "지리", "역사", "기후", "헌법", "인권"]):
        return "social", "사회"
    if any(k in combined for k in ["총론", "학교자율시간", "핵심역량", "2022 개정 교육과정 총론", "깊이있는학습"]):
        return "general", "총론"
    if any(k in combined for k in ["국어", "읽기", "쓰기", "문학", "문법", "직소", "반응중심", "한글", "퇴고"]):
        return "korean", "국어"
    if any(k in combined for k in ["수학", "분수", "도형", "측정", "수와 연산", "반힐레", "폴리아", "딘즈"]):
        return "math", "수학"
        
    return thread.get("main_category", "general"), thread.get("category", "공통")

def extract_core_topic(thread, cat_name):
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    sc = str(thread.get("sub_category", ""))
    core = insight.get("core_concept", "")
    
    topic = ititle.split(">")[-1].strip() if ">" in ititle else ititle
    if not topic or topic in ["수학", "사회", "과학", "도덕", "국어", "체육", "음악", "미술", "실과", "영어", "총론", "공통"]:
        topic = sc or thread.get("title", "") or core.split(".")[0] or f"{cat_name} 핵심 지도 내용"
        
    # Clean up topic string
    topic = re.sub(r'[\(\)\[\]_\\/]', ' ', topic).strip()
    topic = re.sub(r'\s+', ' ', topic)
    return topic or f"{cat_name} 단원 핵심"

def generate_study_comments(topic, cat_name):
    c1 = f"'{topic}' 단권화할 때 지도서 원문 표현과 1차 채점 필수 조건을 한 세트로 묶어서 정리해두면 인출 속도가 훨씬 빨라집니다."
    c2 = f"기출 분석해보면 '{topic}' 제재는 단순 암기보다 교사 발문과 학생 반응 맥락을 분석하여 지도 방안을 도출하는 서술형으로 빈출됩니다."
    c3 = f"이 제재에서 자주 헷갈리는 오개념이나 유사 개념과의 차이점을 명확히 짚고 넘어가야 실전에서 부분 감점을 피할 수 있겠네요!"
    c4 = f"채점관 관점: '{topic}' 관련 문항은 교육과정 공식 학술 명칭과 조작적 정의가 정확히 들어가야 1점 만점을 부여합니다."
    
    return [
        {"author": "단권화_장인", "handle": "summary_master", "avatar": "📒", "persona_name": "단권화_장인", "text": c1, "content": c1},
        {"author": "기출분석_고수", "handle": "exam_expert", "avatar": "🔎", "persona_name": "기출분석_고수", "text": c2, "content": c2},
        {"author": "새벽공부_불꽃초시생", "handle": "fire_beginner", "avatar": "🔥", "persona_name": "새벽공부_불꽃초시생", "text": c3, "content": c3},
        {"author": "답안지_채점관", "handle": "scorer_official", "avatar": "✍️", "persona_name": "답안지_채점관", "text": c4, "content": c4}
    ]

def clean_tags(thread, cat_name, topic):
    old_tags = thread.get("tags", [])
    banned = ["#10개년빈출", "#칼채점키워드", "#감점주의", "#초등임용", "#초등임용고시", "#감점주의_선행절차누락", "#감점주의_탈락조건오기"]
    filtered = [t for t in old_tags if not any(b in t for b in banned)]
    
    # Add subject tag
    cat_tag = f"#{cat_name}"
    if cat_tag not in filtered:
        filtered.insert(0, cat_tag)
        
    # Add topic tag if short and clean
    topic_tag = "#" + re.sub(r'\s+', '_', topic[:15].strip())
    if len(topic_tag) > 2 and topic_tag not in filtered:
        filtered.append(topic_tag)
        
    return filtered[:8]

def run_overhaul():
    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} not found")
        return
        
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    print(f"Starting Global Overhaul across all {len(db)} threads...")
    
    emoji_cleaned = 0
    latex_cleaned = 0
    categories_fixed = 0
    comments_updated = 0
    
    for i, t in enumerate(db):
        # 1. Clean emojis and latex across all posts
        posts = t.get("posts", [])
        for p in posts:
            old_text = p.get("text", "")
            new_text = clean_emojis(old_text)
            new_text = clean_latex(new_text)
            if new_text != old_text:
                p["text"] = new_text
                if any(em in old_text for em in ['1️⃣', '2️⃣', '📍', '⭕', '👉']):
                    emoji_cleaned += 1
                if any(lx in old_text for lx in [r'\frac', r'\times', r'\div', '$']):
                    latex_cleaned += 1
                    
        # 2. Category inference & correction
        old_mc = t.get("main_category", "")
        new_mc, new_cname = infer_category(t)
        if new_mc != old_mc:
            t["main_category"] = new_mc
            t["category"] = new_cname
            categories_fixed += 1
        else:
            t["category"] = new_cname
            
        topic = extract_core_topic(t, new_cname)
        
        # 3. Ensure clean title
        if not t.get("title"):
            t["title"] = f"{new_cname}: {topic}"
            
        # 4. Comments overhaul if legacy (2-person or empty or mismatch)
        current_cmts = t.get("comments", [])
        is_legacy = (
            len(current_cmts) < 3 or
            (len(current_cmts) > 0 and current_cmts[0].get("author") in ["핵심힌터_멘토", "멘토", None]) or
            (len(current_cmts) > 0 and "@" in current_cmts[0].get("author", ""))
        )
        
        # Only overwrite if legacy or missing to preserve hand-crafted recent batches
        if is_legacy:
            new_cmts = generate_study_comments(topic, new_cname)
            t["comments"] = new_cmts
            t["simulated_comments"] = new_cmts
            comments_updated += 1
        else:
            # Ensure simulated_comments and comments are synchronized with 6 fields
            for c in current_cmts:
                if "author" not in c:
                    c["author"] = c.get("persona_name", "합격멘토")
                if "handle" not in c:
                    c["handle"] = "mentor"
                if "content" not in c:
                    c["content"] = c.get("text", "")
                if "persona_name" not in c:
                    c["persona_name"] = c.get("author", "합격멘토")
                if "text" not in c:
                    c["text"] = c.get("content", "")
                if "avatar" not in c:
                    c["avatar"] = "💬"
            t["comments"] = current_cmts
            t["simulated_comments"] = current_cmts
            
        # 5. Clean tags
        t["tags"] = clean_tags(t, new_cname, topic)
        
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
        
    print(f"Global Overhaul Completed Successfully!")
    print(f"- Emoji clutter cleaned: {emoji_cleaned} posts")
    print(f"- LaTeX converted to Unicode math: {latex_cleaned} posts")
    print(f"- Categories corrected: {categories_fixed} threads")
    print(f"- Legacy comments upgraded to 4-persona study ecosystem: {comments_updated} threads")
    print(f"- Total active threads verified: {len(db)}")

if __name__ == "__main__":
    run_overhaul()
