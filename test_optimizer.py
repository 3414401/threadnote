#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Global Thread Optimizer (Token-Zero Architecture)
- Strips emoji clutter (1️⃣, 2️⃣, 📍, etc.) across all posts
- Converts raw LaTeX math to clean Unicode math
- Corrects mistagged categories based on content
- Overhauls legacy 2-person boilerplate comments into 4 authentic, topic-specific study personas
- Ensures structural line breaks and bold keywords
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

def clean_emojis_and_lists(text):
    if not isinstance(text, str):
        return text
    
    # Remove repetitive list numbers like 1️⃣, 2️⃣, 3️⃣, etc. and 📍, ⭕, 👉, ▶️, ➗
    # If at the start of a line or heading:
    text = re.sub(r'^[ \t]*[1-9]️⃣[ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*🔟[ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*[📍⭕👉▶️➗▪️▫️■□][ \t]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'([ \n])[1-9]️⃣[ \t]*', r'\1', text)
    text = re.sub(r'([ \n])🔟[ \t]*', r'\1', text)
    text = re.sub(r'([ \n])[📍⭕👉▶️➗▪️▫️■□][ \t]*', r'\1', text)
    
    # Strip any trailing emoji clutter in posts
    # Keep single 💡 or ⚠️ at the start of takeaway/tips
    return text.strip()

def clean_latex_math(text):
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
    # Check insight title first
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    sc = thread.get("sub_category", "")
    quote = insight.get("academic_quote", "")
    posts_text = " ".join([p.get("text", "") for p in thread.get("posts", [])[:2]])
    combined = f"{ititle} {sc} {quote} {posts_text}"
    
    for kw, (cat_id, cat_name) in CATEGORY_MAP.items():
        if ititle.startswith(kw) or f"{kw} >" in ititle or f"{kw}과" in ititle:
            return cat_id, cat_name
            
    # Secondary check on keywords
    if any(k in combined for k in ["도덕", "콜버그", "피아제", "배려윤리", "인격교육", "도덕성"]):
        return "moral", "도덕"
    if any(k in combined for k in ["미술", "로웬펠드", "펠드만", "판화", "조형", "감상", "회화"]):
        return "art", "미술"
    if any(k in combined for k in ["음악", "달크로즈", "코다이", "오르프", "고든", "장단", "오스티나토", "가창"]):
        return "music", "음악"
    if any(k in combined for k in ["체육", "PAPS", "TGfU", "라반", "스포츠", "도전영역", "경쟁영역"]):
        return "pe", "체육"
    if any(k in combined for k in ["실과", "식생활", "식품구성자전거", "스마트팜", "홈프로젝트", "수송기술", "발명"]):
        return "practical_arts", "실과"
    if any(k in combined for k in ["영어", "CLT", "TBLT", "크라센", "스웨인", "PPP모형", "파닉스"]):
        return "english", "영어"
    if any(k in combined for k in ["과학", "달의", "태양", "광합성", "5E", "POE", "순환학습", "가설검증"]):
        return "science", "과학"
    if any(k in combined for k in ["사회", "민주주의", "다수결", "논쟁문제", "의사결정", "지리", "역사"]):
        return "social", "사회"
    if any(k in combined for k in ["총론", "학교자율시간", "핵심역량", "2022 개정 교육과정 총론"]):
        return "general", "총론"
    if any(k in combined for k in ["국어", "읽기", "쓰기", "문학", "문법", "직소", "반응중심"]):
        return "korean", "국어"
    if any(k in combined for k in ["수학", "분수", "도형", "측정", "수와 연산", "반힐레"]):
        return "math", "수학"
        
    # Default fallback to existing
    mc = thread.get("main_category", "general")
    c = thread.get("category", "공통")
    return mc, c

def generate_topic_comments(thread, cat_name):
    insight = thread.get("source_insight", {})
    ititle = insight.get("title", "")
    core = insight.get("core_concept", "")
    quote = insight.get("academic_quote", "")
    
    # Topic label
    topic = ititle.split(">")[-1].strip() if ">" in ititle else ititle
    if not topic or topic in ["수학", "사회", "과학", "도덕", "국어", "체육", "음악", "미술", "실과", "영어", "총론"]:
        topic = thread.get("sub_category", "") or thread.get("title", "") or f"{cat_name} 핵심 제재"
        
    topic_clean = re.sub(r'[\\/()_]', ' ', topic).strip()
    
    # Construct 4 rich, distinct comments
    c1 = f"'{topic_clean}' 단권화할 때 지도서 원문 표현과 1차 필수 조건을 한 세트로 묶어서 정리해두면 인출 속도가 훨씬 빨라집니다."
    c2 = f"기출 분석해보면 '{topic_clean}' 제재는 단순 암기보다 교사 발문과 학생 반응 맥락을 분석하여 지도 방안을 도출하는 서술형으로 빈출됩니다."
    c3 = f"이 제재에서 자주 헷갈리는 오개념이나 유사 개념과의 차이점을 명확히 짚고 넘어가야 실전에서 부분 감점을 피할 수 있겠네요!"
    c4 = f"채점관 관점: '{topic_clean}' 관련 문항은 교육과정 공식 학술 명칭과 조작적 정의가 정확히 들어가야 1점 만점을 부여합니다."
    
    return [
        {"author": "단권화_장인", "handle": "summary_master", "avatar": "📒", "persona_name": "단권화_장인", "text": c1, "content": c1},
        {"author": "기출분석_고수", "handle": "exam_expert", "avatar": "🔎", "persona_name": "기출분석_고수", "text": c2, "content": c2},
        {"author": "새벽공부_불꽃초시생", "handle": "fire_beginner", "avatar": "🔥", "persona_name": "새벽공부_불꽃초시생", "text": c3, "content": c3},
        {"author": "답안지_채점관", "handle": "scorer_official", "avatar": "✍️", "persona_name": "답안지_채점관", "text": c4, "content": c4}
    ]

def clean_tags(thread, cat_name):
    old_tags = thread.get("tags", [])
    banned = ["#10개년빈출", "#칼채점키워드", "#감점주의", "#초등임용", "#초등임용고시"]
    filtered = [t for t in old_tags if not any(b in t for b in banned)]
    
    # Add subject tag if missing
    cat_tag = f"#{cat_name}"
    if cat_tag not in filtered:
        filtered.insert(0, cat_tag)
        
    return filtered[:8]

def test_run():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    print(f"Loaded {len(db)} threads. Testing on threads 252 to 255...")
    for idx in range(252, 256):
        t = db[idx]
        cat_id, cat_name = infer_category(t)
        print(f"[{idx}] {t.get('thread_id')} -> {cat_id} ({cat_name})")
        cmts = generate_topic_comments(t, cat_name)
        print("  Sample Comment 0:", cmts[0]["author"], "|", cmts[0]["text"])

if __name__ == "__main__":
    test_run()
