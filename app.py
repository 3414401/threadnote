#!/usr/bin/env python3
"""
ThreadNote (지식스레드) - Meta Threads App Clone Backend
Features:
- PDF Upload processing via macOS native PDFKit
- Auto-feed refresh upon document upload
- Infinite scroll feed generation with endless educational stories & pedagogical insights
"""

import base64
import ctypes
from ctypes import c_void_p, c_char_p, c_ulong
import http.server
import json
import os
import random
import re
import socketserver
import sys
import urllib.parse
from datetime import datetime

try:
    import psycopg
    from psycopg.types.json import Jsonb
except ImportError:
    psycopg = None
    Jsonb = None

PORT = int(os.environ.get("PORT", 8765))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
SAMPLES_DIR = os.path.join(BASE_DIR, "samples")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
CATEGORIES_FILE = os.path.join(UPLOADS_DIR, "categories.json")
USER_THREADS_FILE = os.path.join(UPLOADS_DIR, "user_threads.json")
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()

os.makedirs(UPLOADS_DIR, exist_ok=True)

## Master Personas (16 Personas) & Master Threads Dataset (42+ Threads)
from curriculum_threads_dataset import PERSONA_PROFILES, ALL_CURRICULUM_THREADS

INITIAL_CURRICULUM_THREADS = ALL_CURRICULUM_THREADS
CURRICULUM_PRELOADED_THREADS = INITIAL_CURRICULUM_THREADS


def load_categories():
    """Load category structure from categories.json"""
    try:
        with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"main_categories": [], "sub_categories": {}, "category_mapping": {}}


def save_categories(data):
    """Save category structure to categories.json"""
    with open(CATEGORIES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_user_threads():
    """Load persistently stored user-uploaded threads"""
    try:
        with open(USER_THREADS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_user_threads(threads):
    """Save user threads to user_threads.json"""
    with open(USER_THREADS_FILE, "w", encoding="utf-8") as f:
        json.dump(threads, f, ensure_ascii=False, indent=2)


def init_likes_db():
    """Create the single-user likes table when a PostgreSQL database is configured."""
    if not DATABASE_URL or psycopg is None:
        return
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS liked_threads (
                thread_id TEXT PRIMARY KEY,
                thread_data JSONB NOT NULL,
                liked_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
        """)


def get_liked_threads():
    """Return all liked thread snapshots, newest first."""
    if not DATABASE_URL or psycopg is None:
        raise RuntimeError("DATABASE_URL 또는 psycopg가 설정되지 않았습니다.")
    with psycopg.connect(DATABASE_URL) as conn:
        rows = conn.execute(
            "SELECT thread_data FROM liked_threads ORDER BY liked_at DESC"
        ).fetchall()
    return [row[0] for row in rows]


def upsert_liked_thread(thread):
    """Store/update one liked thread snapshot."""
    if not DATABASE_URL or psycopg is None:
        raise RuntimeError("DATABASE_URL 또는 psycopg가 설정되지 않았습니다.")
    thread_id = str(thread.get("thread_id", "")).strip()
    if not thread_id:
        raise ValueError("thread_id가 필요합니다.")
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute(
            """
            INSERT INTO liked_threads (thread_id, thread_data, liked_at)
            VALUES (%s, %s, NOW())
            ON CONFLICT (thread_id)
            DO UPDATE SET thread_data = EXCLUDED.thread_data, liked_at = NOW()
            """,
            (thread_id, Jsonb(thread))
        )


def delete_liked_thread(thread_id):
    """Remove one liked thread."""
    if not DATABASE_URL or psycopg is None:
        raise RuntimeError("DATABASE_URL 또는 psycopg가 설정되지 않았습니다.")
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("DELETE FROM liked_threads WHERE thread_id = %s", (thread_id,))


def get_main_category(thread, cat_mapping):
    """Resolve main_category for a thread using category_mapping"""
    # If thread already has main_category field, use it
    if thread.get("main_category"):
        return thread["main_category"]
    # Fall back to category_mapping
    cat = thread.get("category", "")
    mapped = cat_mapping.get(cat, {})
    return mapped.get("main", "math")


def get_sub_category(thread, cat_mapping):
    """Resolve sub_category for a thread"""
    if thread.get("sub_category"):
        return thread["sub_category"]
    cat = thread.get("category", "")
    mapped = cat_mapping.get(cat, {})
    return mapped.get("sub", "")


def parse_thread_txt(text: str):
    """
    Parse TXT file into list of thread dicts.
    Format:
      ===THREAD===
      대분류: 수학
      소분류: 도형
      글쓴이: 홍길동 선생님
      아바타: 👨‍🏫
      태그: #tag1 #tag2

      [훅]
      ...

      [핵심]
      ...

      [실천]
      ...

      [댓글]
      😄 닉네임: 댓글내용
      ===END===
    """
    threads = []
    # Split into thread blocks
    blocks = re.split(r'===THREAD===', text, flags=re.IGNORECASE)
    for block in blocks:
        if '===END===' not in block.upper():
            continue
        block = block[:block.upper().index('===END===')]

        meta = {}
        posts = []
        comments = []
        current_section = None
        current_text = []

        for line in block.splitlines():
            stripped = line.strip()

            # Skip generic marker like [본문], content:
            if re.match(r'^(?:\[본문\]|content\s*:?)$', stripped, re.IGNORECASE):
                continue

            # Parse metadata lines (key: value or [key] value, Korean or English, with optional # or -)
            if current_section is None:
                m = re.match(r'^(?:[-*#•\s]*)(?:\[)?(대분류|소분류|분류|과목|글쓴이|아바타|태그|출제포인트|지도서원문|성취기준|학년군|오개념|category|sub_category|subject|author|avatar|tags|points|document|achievement|grade|misconception|title|id)(?:\])?\s*[:=]?\s*(.+)$', stripped, re.IGNORECASE)
                if m:
                    raw_k = m.group(1).lower()
                    val = m.group(2).strip()
                    key_map = {
                        "category": "대분류", "분류": "대분류", "과목": "대분류", "subject": "대분류",
                        "author": "글쓴이", "avatar": "아바타", "tags": "태그",
                        "points": "출제포인트", "document": "지도서원문", "achievement": "성취기준",
                        "grade": "학년군", "misconception": "오개념", "sub_category": "소분류"
                    }
                    k_target = key_map.get(raw_k, m.group(1))
                    if k_target == "대분류" and "|" in val:
                        parts = [p.strip() for p in val.split("|")]
                        meta["대분류"] = parts[0]
                        if len(parts) > 1 and parts[1]:
                            meta["소분류"] = parts[1]
                        if len(parts) > 2 and parts[2]:
                            meta["글쓴이"] = parts[2]
                    else:
                        meta[k_target] = val
                    continue

            # Section headers (flexible matching with optional inline text)
            m_hook = re.match(r'^\[훅\]\s*(.*)$', stripped, re.IGNORECASE)
            m_twist = re.match(r'^\[핵심\]\s*(.*)$', stripped, re.IGNORECASE)
            m_action = re.match(r'^\[실천\]\s*(.*)$', stripped, re.IGNORECASE)
            m_comment_hdr = re.match(r'^\[댓글\]\s*(.*)$', stripped, re.IGNORECASE)

            if m_hook:
                if current_section and current_text:
                    posts.append((current_section, "\n".join(current_text).strip()))
                current_section = "hook"
                current_text = [m_hook.group(1).strip()] if m_hook.group(1).strip() else []
            elif m_twist:
                if current_section and current_text:
                    posts.append((current_section, "\n".join(current_text).strip()))
                current_section = "twist"
                current_text = [m_twist.group(1).strip()] if m_twist.group(1).strip() else []
            elif m_action:
                if current_section and current_text:
                    posts.append((current_section, "\n".join(current_text).strip()))
                current_section = "action"
                current_text = [m_action.group(1).strip()] if m_action.group(1).strip() else []
            elif m_comment_hdr:
                if current_section and current_text:
                    posts.append((current_section, "\n".join(current_text).strip()))
                current_section = "comments"
                current_text = []
            elif current_section == "comments":
                # Each line is a comment: optional dash, optional avatar/emoji, name: text
                cleaned_line = re.sub(r'^[-*•]\s*', '', stripped)
                cm = re.match(r'^(?:(\S+)\s+)?([^:]+):\s*(.+)$', cleaned_line)
                if cm:
                    first_tok = cm.group(1) or "💬"
                    p_name = cm.group(2).strip()
                    c_text = cm.group(3).strip()
                    # if first token doesn't look like emoji or is part of name
                    if len(first_tok) > 2 and not any(ord(c) > 0x1F000 for c in first_tok):
                        p_name = f"{first_tok} {p_name}".strip()
                        first_tok = "💬"
                    comments.append({
                        "avatar": first_tok,
                        "persona_name": p_name,
                        "text": c_text
                    })
            elif current_section:
                if stripped:
                    current_text.append(stripped)

        # Flush last section
        if current_section and current_section != "comments" and current_text:
            posts.append((current_section, "\n".join(current_text).strip()))

        if not posts:
            continue

        # Build category info
        main_label = meta.get("대분류", "수학")
        sub_label = meta.get("소분류", "")
        author_name = meta.get("글쓴이", "익명 선생님")
        avatar = meta.get("아바타", "📝")
        tags_raw = meta.get("태그", "")
        tags = tags_raw.split() if tags_raw else []

        # Map main_label to main_category id
        main_id_map = {
            "국어": "korean", "수학": "math", "영어": "english",
            "사회": "social", "과학": "science", "음악": "music",
            "총론": "general", "미술": "art", "실과": "tech",
            "통합": "integrated", "체육": "pe", "도덕": "moral", "창체": "creative"
        }
        main_id = "math"
        for k, v in main_id_map.items():
            if k in main_label:
                main_id = v
                main_label = k  # Normalize label (e.g. '국어과 교육과정' -> '국어')
                break

        thread_posts = []
        type_map = {"hook": "hook", "twist": "twist", "action": "action"}
        for role, txt in posts:
            thread_posts.append({"text": txt, "type": type_map.get(role, role)})

        tid = f"user_{int(datetime.now().timestamp() * 1000)}_{random.randint(100,999)}"
        thread = {
            "thread_id": tid,
            "main_category": main_id,
            "sub_category": sub_label,
            "category": main_label,
            "persona": {
                "id": "user_upload",
                "name": author_name,
                "handle": re.sub(r'\s+', '_', author_name.lower()),
                "avatar": avatar,
                "badge": "업로드 스레드",
                "followers": "0"
            },
            "subject_tag": main_label,
            "timestamp": "방금 전",
            "likes": random.randint(10, 200),
            "replies": random.randint(0, 20),
            "reposts": random.randint(0, 15),
            "posts": thread_posts,
            "tags": tags,
            "source_insight": {
                "title": f"{main_label} > {sub_label}" if sub_label else main_label,
                "grade": meta.get("학년군", "초등 3~6학년군"),
                "academic_quote": meta.get("지도서원문", meta.get("오개념", "2022 개정 교육과정 교수·학습 방법 및 유의사항 참조")),
                "curriculum_code": meta.get("성취기준", "2022 개정 초등 교육과정"),
                "core_concept": meta.get("출제포인트", f"{main_label} 핵심 지도 요령 및 오개념 지도")
            },
            "simulated_comments": comments
        }
        threads.append(thread)

    return threads

# Additional Curriculum Topics Pool for Infinite Scroll Generation
INFINITE_TOPICS_POOL = [
    {
        "title": "03 소수의 크기 비교 (4-2)",
        "category": "수와 연산",
        "grade": "3~4학년군",
        "hook": "오늘 초등 4학년 시험지에서 0.6 vs 0.60 크기 비교 물어봤다가 교실 뒤집어진 썰 🧵👇",
        "twist": "애들이 '0.60이 세 글자니까 0.6보다 더 커요!'라고 당당하게 외침 ㅋㅋㅋ\n자연수에서는 자릿수가 길수록 큰 수가 맞지만, 소수에서는 0.6은 10개 중 6개, 0.60은 100개 중 60개라서 양이 완전히 똑같음!\n(오개념) 더 긴 수가 더 큰 소수다 -> 지도서 필수 지적 사항!",
        "action": "지도 팁: 자릿값 판을 활용해서 일의 자리부터 소수 첫째, 둘째 자리 차례대로 비교하게 훈련시키기!",
        "quote": "[오류] 더 긴 수가 더 큰 소수다. 원인: 소수의 자릿값 개념 부족. 지도: 수직선 모델 및 영역 모델 활용.",
        "concept": "소수의 위치적 기수법과 동치 소수(Equivalent Decimals)"
    },
    {
        "title": "02. 동치 관계와 등호(=)의 오개념 (4-1)",
        "category": "수와 연산",
        "grade": "3~4학년군",
        "hook": "초등 4학년 애들한테 '8 + 4 = [ ] + 5' 문제 내면 10명 중 9명이 빈칸에 '12'를 쓰는 충격적인 이유 🧵👇",
        "twist": "등호(=)를 '양쪽이 평형을 이루는 저울(동치 관계)'로 안 보고, '계산 버튼(Enter 키)'으로 생각하기 때문임!\n8+4를 보자마자 12 쓰고, 뒤에 +5는 쳐다도 안 봄 ㅋㅋㅋ\n이게 바로 등호의 연산적 오류!",
        "action": "해결책: 양팔 저울 모델로 왼쪽 저울에 8과 4를 올렸으면 오른쪽도 12가 되어야 하므로 빈칸은 7이라는 '관계적 사고'를 길러줘야 함.",
        "quote": "등호의 의미: 연산의 결과가 아닌 '관계적 의미(동치 관계)'. 8 + 4 = [] + 5 에서 빈칸에 12를 쓰는 오류 지도.",
        "concept": "대수적 사고의 출발점인 등호의 관계적 의미(Relational meaning of equals sign)"
    },
    {
        "title": "06-01 다각형의 둘레와 넓이의 관계 (5-1)",
        "category": "측정",
        "grade": "5~6학년군",
        "hook": "성인들도 90% 이상 낚이는 초등 5학년 기하학 함정 문제 🧵👇\n'둘레가 길어지면 넓이도 무조건 넓어질까요?'",
        "twist": "정답은 '전혀 아니다'입니다!\n가로 1cm, 세로 100cm인 직사각형은 둘레가 202cm지만 넓이는 고작 100㎠임.\n반면 가로 10cm, 세로 10cm인 정사각형은 둘레가 40cm밖에 안 되는데 넓이가 100㎠로 똑같음!\n모양이 납작해질수록 둘레만 커지고 실속(넓이)은 줄어드는 원리.",
        "action": "생활 팁: 같은 양의 울타리(둘레)로 가장 넓은 마당을 만들고 싶다면 정사각형이나 원 모양으로 둘러쳐야 합니다!",
        "quote": "둘레와 넓이 학습의 오개념: 1) 둘레가 길면 넓이가 크다. 2) 넓이가 크면 둘레도 길다.",
        "concept": "둘레와 넓이의 독립성 및 등주부등식(Isoperimetric inequality)의 직관적 이해"
    },
    {
        "title": "04 시각과 시간의 차이 (2-2)",
        "category": "측정",
        "grade": "1~2학년군",
        "hook": "출근길에 지하철 시계 보면서 문득 든 생각. 우리는 왜 '시각'과 '시간'을 매일 헷갈릴까? 🧵👇",
        "twist": "'지금 몇 시 몇 분이야?'는 위치를 묻는 [시각]이고, '여기서 강남역까지 얼마나 걸려?'는 두 시각 사이의 양(거리)인 [시간]임!\n그래서 '시각 + 시각'은 물리적으로 불가능(3시 + 5시 = ?)\n하지만 '시각 + 시간'은 가능(3시에 2시간 지나면 5시)!",
        "action": "초등 2학년 지도서 팁: 1주일은 요일 순서와 상관없이 7일이라는 시간의 양임을 시간 띠 모델로 시각화하기.",
        "quote": "시각: 시침, 분침이 가리키는 때의 위치. 시간: 두 시각 사이의 거리인 양. 시각끼리의 덧셈은 불가능.",
        "concept": "시각(Time instant)과 시간(Duration)의 개념적 구별 및 60진법 덧셈"
    },
    {
        "title": "04. 비와 비율 (6-1)",
        "category": "수와 연산",
        "grade": "5~6학년군",
        "hook": "축구 경기 볼 때 '4 대 1'을 어떻게 읽으시나요? 초등 6학년 지도서에 나온 4가지 읽기법 🧵👇",
        "twist": "1) 4와 1의 비\n2) 1에 대한 4의 비\n3) 4의 1에 대한 비\n4) 4 대 1\n여기서 핵심: '~에 대한'이 붙은 쪽이 바로 분모가 되는 [기준량]이라는 점!\n기준량이 무엇인지 모르면 중고등학교 통계와 물리에서 백프로 멘붕 옵니다.",
        "action": "팁: 할인율 20%란 원래 가격(기준량)에 대한 할인된 금액(비교하는 양)의 비율이라는 점을 쇼핑할 때마다 되새겨보세요!",
        "quote": "[6수02-02] 기준량과 비교하는 양을 명확하게 인식하게 하기. 기호(:)의 오른쪽에 있는 수가 기준량.",
        "concept": "상대적 비교(승법적 관계)로서의 비와 비율(Ratio and Proportion)"
    },
    {
        "title": "06-02 원주율과 원의 넓이 (6-2)",
        "category": "도형",
        "grade": "5~6학년군",
        "hook": "초등 6학년들이 컴퍼스 들고 원주율 3.14를 직접 손으로 찾아내는 눈물겨운 여정 🧵👇",
        "twist": "원 안에 꼭 맞는 정육각형 둘레 = 지름의 3배.\n원 밖을 감싸는 정사각형 둘레 = 지름의 4배.\n따라서 원의 둘레는 무조건 '지름의 3배보다 크고 4배보다 작다'는 진리가 바로 도출됨!\n이걸 정96각형까지 쪼개서 아르키메데스가 찾아낸 게 3.14159...",
        "action": "시험 꿀팁: 원을 무수히 잘게 잘라 엇갈려 붙이면 직사각형이 되는데, 그 직사각형의 가로가 (원주율 × 반지름), 세로가 (반반지름)이라 원의 넓이 공식이 나옴!",
        "quote": "원주 어림하기: 지름의 3배 < 원주 < 지름의 4배. 원을 잘라 직사각형으로 바꾸어 넓이 구하기(등적 변형).",
        "concept": "극한 개념의 초등화: 구분구적법과 등적 변형을 통한 원주율 유도"
    },
    {
        "title": "대각선의 정의와 삼각형 (4-2)",
        "category": "도형",
        "grade": "3~4학년군",
        "hook": "초등 4학년 수학 퀴즈: '삼각형은 왜 대각선이 0개일까요?' 🧵👇",
        "twist": "공식 n(n-3)/2 에 3 넣으면 0이라서? NO!\n대각선의 수학적 정의는 '서로 이웃하지 않는 두 꼭짓점을 이은 선분'임.\n근데 삼각형은 꼭짓점이 3개뿐이라, 어떤 두 점을 잡아도 무조건 '이웃한 꼭짓점'임 ㅋㅋㅋ\n이웃하지 않는 꼭짓점이 아예 존재하지 않기 때문에 대각선을 그을 수 없는 거임!",
        "action": "생각의 전환: 공식에 숫자를 대입하기 전에 '정의의 본질'을 한 번만 곱씹어보세요.",
        "quote": "대각선: 다각형에서 서로 이웃하지 않는 두 꼭짓점을 이은 선분. Q. 삼각형의 대각선을 그을 수 없는 이유? A. 서로 이웃하지 않는 두 꼭짓점이 없기 때문이다.",
        "concept": "기하학적 공리 정의와 반례 부재의 원리"
    },
    {
        "title": "쌓기나무와 보이지 않는 개수 (6-2)",
        "category": "도형",
        "grade": "5~6학년군",
        "hook": "오늘 쌓기나무 수업하다가 '선생님 답이 왜 2개예요?' 질문받고 감동한 썰 🧵👇",
        "twist": "위, 앞, 옆에서 본 그림만 주어지면 겉으로 안 보이는 사각지대에 쌓기나무가 1개 숨어있을 수도 있고 없을 수도 있음!\n초등 각론에서는 이걸 '공간 시각화'라고 부름.\n보이지 않는 것을 머릿속에서 회전시키고 뒤집어보는 능력!",
        "action": "공간 감각 기르기: 전개도를 보고 머릿속으로 접어서 입체도형을 상상하는 훈련이 메타인지 향상의 지름길입니다.",
        "quote": "투영도: 보이지 않는 선을 나타내지 않음. 여러 가지 답이 나오는 이유: 보이지 않는 쌓기나무의 개수를 정확하게 알 수 없음.",
        "concept": "공간 시각화(Spatial Visualization)와 공간 방향(Spatial Orientation)"
    }
]

# Active pool = curriculum threads + persisted user uploads
ACTIVE_KNOWLEDGE_POOL = list(INITIAL_CURRICULUM_THREADS) + load_user_threads()


def extract_pdf_native(pdf_path: str) -> str:
    """
    Extracts complete text from any PDF using macOS native PDFKit via ctypes.
    Completely zero dependency, fast, handles Korean text perfectly.
    """
    try:
        objc = ctypes.cdll.LoadLibrary('/usr/lib/libobjc.A.dylib')
        objc.objc_getClass.restype = c_void_p
        objc.objc_getClass.argtypes = [c_char_p]
        objc.sel_registerName.restype = c_void_p
        objc.sel_registerName.argtypes = [c_char_p]
        msg_send = objc.objc_msgSend

        ctypes.cdll.LoadLibrary('/System/Library/Frameworks/PDFKit.framework/PDFKit')
        ctypes.cdll.LoadLibrary('/System/Library/Frameworks/Foundation.framework/Foundation')

        PDFDocument = objc.objc_getClass(b'PDFDocument')
        NSURL = objc.objc_getClass(b'NSURL')
        NSString = objc.objc_getClass(b'NSString')

        msg_send.restype = c_void_p
        msg_send.argtypes = [c_void_p, c_void_p, c_char_p]
        ns_path = msg_send(NSString, objc.sel_registerName(b'stringWithUTF8String:'), pdf_path.encode('utf-8'))

        msg_send.argtypes = [c_void_p, c_void_p, c_void_p]
        url = msg_send(NSURL, objc.sel_registerName(b'fileURLWithPath:'), ns_path)

        msg_send.argtypes = [c_void_p, c_void_p]
        alloc_doc = msg_send(PDFDocument, objc.sel_registerName(b'alloc'))

        msg_send.argtypes = [c_void_p, c_void_p, c_void_p]
        doc = msg_send(alloc_doc, objc.sel_registerName(b'initWithURL:'), url)

        if not doc:
            return ""

        msg_send.restype = c_void_p
        msg_send.argtypes = [c_void_p, c_void_p]
        doc_string = msg_send(doc, objc.sel_registerName(b'string'))

        if not doc_string:
            return ""

        msg_send.restype = c_char_p
        msg_send.argtypes = [c_void_p, c_void_p]
        utf8_str = msg_send(doc_string, objc.sel_registerName(b'UTF8String'))
        if utf8_str:
            return utf8_str.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Native PDF extraction warning: {e}")
    return ""


def parse_curriculum_sections(text: str):
    """
    Parses sections, achievements, misconceptions, and pedagogical Q&As from curriculum notes.
    """
    sections = []
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    current_sec = None
    for line in lines:
        if re.match(r'^(?:\d+\.|\d+-\d+\.|\d+\s+[가-힣]+)', line):
            if current_sec and (current_sec["content"] or current_sec["misconceptions"]):
                sections.append(current_sec)
            current_sec = {
                "title": line.replace("+", "").strip(),
                "content": [],
                "misconceptions": [],
                "qna": [],
                "cautions": []
            }
        else:
            if not current_sec:
                current_sec = {
                    "title": line.replace("+", "").strip(),
                    "content": [],
                    "misconceptions": [],
                    "qna": [],
                    "cautions": []
                }
            else:
                current_sec["content"].append(line)
                if "(오)" in line:
                    current_sec["misconceptions"].append(line)
                elif line.startswith("Q.") or line.startswith("Q :"):
                    current_sec["qna"].append(line)
                elif "[유의점]" in line or "유의 :" in line:
                    current_sec["cautions"].append(line)

    if current_sec and (current_sec["content"] or current_sec["misconceptions"]):
        sections.append(current_sec)

    return sections


def generate_curriculum_thread(section_data, persona_id="elementary_teacher", custom_style=""):
    """
    Transforms an extracted curriculum section into a vivid Threads post.
    """
    title = section_data.get("title", "초등수학 지식")
    content_lines = section_data.get("content", [])
    raw_snippet = " ".join(content_lines[:15]) if content_lines else title
    
    misconceptions = section_data.get("misconceptions", [])
    qna = section_data.get("qna", [])

    persona = PERSONA_PROFILES.get(persona_id, PERSONA_PROFILES["elementary_teacher"])
    
    hook = f"오늘 {title} 관련해서 교실에서 겪은 충격적인 썰 🧵👇\n\n" \
           f"교과서로 볼 땐 그냥 지나치기 쉬운데, 지도서 각론을 깊게 파보면 " \
           f"아이들이 왜 여기서 막히는지 그 이유가 적나라하게 적혀 있음 ㅠㅠ"

    twist = f"핵심은 바로 이겁니다.\n\n" \
            f"『{title}』에서 가장 중요한 교수학적 원리:\n" \
            f"\"{raw_snippet[:180]}...\"\n\n"
    if misconceptions:
        twist += f"⚠️ 대표 오개념 경보:\n{misconceptions[0]}\n"
    else:
        twist += "어른들의 시선에서 당연한 공식이라도, 아이들에게는 구체적인 조작 활동(종이접기, 수 모형, 영역 모델)을 거쳐야만 참된 지식이 된다는 것."

    action = f"💡 현장에서 바로 써먹는 수업 & 복습 팁:\n\n" \
             f"1. 암기식 정의보다 '내가 왜 그렇게 생각했는지' 말로 설명하게 하기\n" \
             f"2. 일상 속 친숙한 물건이나 상황으로 연결해보기\n\n" \
             f"임고생이나 초등 학부모님들 꼭 저장해두세요 📌\n" \
             f"여러분은 학창 시절에 이 단원 어떻게 배우셨나요? 댓글로 나눠주세요!"

    thread_id = f"th_{int(datetime.now().timestamp() * 1000)}_{random.randint(100, 999)}"
    likes = random.randint(520, 2400)
    
    category = "도형"
    if any(k in title for k in ["수", "연산", "분수", "소수", "곱셈", "나눗셈"]):
        category = "수와 연산"
    elif any(k in title for k in ["측정", "길이", "시간", "각도", "넓이", "부피", "원주율", "들이"]):
        category = "측정"
    elif any(k in title for k in ["교육론", "스켐프", "디에네스", "브루너", "피아제", "반힐레", "프로이덴탈", "오슈벨", "모형", "가치"]):
        category = "수학교육론"
    elif any(k in title for k in ["국어", "읽기", "문법", "음운", "영어", "Dictogloss", "PPP"]):
        category = "국어·영어"
    elif any(k in title for k in ["사회", "지도", "GIS", "극점", "도덕", "윤리", "칸트", "지역"]):
        category = "사회·도덕"
    elif any(k in title for k in ["과학", "소리", "실험", "실과", "식생활", "식품", "스마트팜"]):
        category = "과학·실과"
    elif any(k in title for k in ["음악", "미술", "체육", "총론", "자율", "장단", "판화", "PAPS"]):
        category = "예체능·총론"
    elif any(k in title for k in ["통합", "봄", "여름", "가을", "겨울", "급식", "오감"]):
        category = "통합교과"

    return {
        "thread_id": thread_id,
        "category": category,
        "grade": "초등 전학년",
        "persona": persona,
        "created_at": "방금 전",
        "metrics": {
            "likes": likes,
            "replies": random.randint(20, 80),
            "reposts": random.randint(40, 210),
            "views": likes * random.randint(4, 8)
        },
        "tags": [f"#{title.replace(' ', '')}", f"#{category}", "#교육과정각론", "#스레드지식"],
        "posts": [
            {"index": 1, "role": "hook", "text": hook},
            {"index": 2, "role": "story_twist", "text": twist},
            {"index": 3, "role": "insight_action", "text": action}
        ],
        "source_insight": {
            "title": title,
            "curriculum_code": "2022 개정 교육과정 수학과 지도서 각론",
            "academic_quote": raw_snippet[:240],
            "core_concept": "발달 단계에 맞춘 수학적 개념 형성 및 오개념 지도 방안",
            "qna": qna[0] if qna else "지도서 핵심 발문 및 지도 유의사항 참조"
        },
        "simulated_comments": [
            {"author": "신규교사1년차", "handle": "newbie_teacher", "avatar": "🌱", "content": "선생님 덕분에 내일 수업 지도안 작성할 때 큰 도움 받았습니다 감사합니다!"},
            {"author": "임고합격기원", "handle": "study_harder", "avatar": "📖", "content": "이거 스터디원들이랑 퀴즈 낼 때 써먹어야겠어요 북마크했습니다!"}
        ]
    }


def synthesize_infinite_thread(topic_idx: int):
    """
    Generates an endless, lively Threads post from the infinite topic pool.
    """
    topic = INFINITE_TOPICS_POOL[topic_idx % len(INFINITE_TOPICS_POOL)]
    personas_keys = list(PERSONA_PROFILES.keys())
    persona_key = personas_keys[(topic_idx + 1) % len(personas_keys)]
    persona = PERSONA_PROFILES[persona_key]

    thread_id = f"th_inf_{topic_idx}"
    likes = random.randint(840, 4800)

    return {
        "thread_id": thread_id,
        "category": topic["category"],
        "grade": topic["grade"],
        "persona": persona,
        "created_at": f"{random.randint(1, 5)}시간 전",
        "metrics": {
            "likes": likes,
            "replies": random.randint(40, 190),
            "reposts": random.randint(90, 480),
            "views": likes * random.randint(4, 9)
        },
        "tags": [f"#{topic['title'].replace(' ', '')}", f"#{topic['category']}", "#수학의신비", "#초등교실썰"],
        "posts": [
            {"index": 1, "role": "hook", "text": topic["hook"]},
            {"index": 2, "role": "story_twist", "text": topic["twist"]},
            {"index": 3, "role": "insight_action", "text": topic["action"]}
        ],
        "source_insight": {
            "title": topic["title"],
            "curriculum_code": "2022 개정 초등수학 지도서",
            "academic_quote": topic["quote"],
            "core_concept": topic["concept"],
            "qna": "지도서 핵심 발문 및 오개념 지도 방안"
        },
        "simulated_comments": [
            {"author": "수학괴물", "handle": "math_monster", "avatar": "📐", "content": "크... 역시 본질을 짚어주시네요. 공감하고 갑니다!"},
            {"author": "초등맘스토리", "handle": "super_mom_edu", "avatar": "🌸", "content": "아이랑 오늘 저녁에 이 이야기 꼭 나눠봐야겠어요 감사합니다!"}
        ]
    }


class ThreadsCloneHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path in ("/api/threads", "/api/feed"):
            page = int(query.get("page", ["1"])[0])
            limit = int(query.get("limit", ["4"])[0])
            main_cat = query.get("main_category", ["all"])[0]
            sub_cat = query.get("sub_category", [""])[0]

            cat_data = load_categories()
            cat_mapping = cat_data.get("category_mapping", {})

            def match(t):
                if main_cat == "all":
                    return True
                t_main = get_main_category(t, cat_mapping)
                if t_main != main_cat:
                    return False
                if sub_cat and sub_cat != "추천":
                    t_sub = get_sub_category(t, cat_mapping)
                    return t_sub == sub_cat
                return True

            
            # Dynamically load latest user threads to pick up auto-generated content
            current_pool = list(INITIAL_CURRICULUM_THREADS) + load_user_threads()
            filtered_pool = [t for t in current_pool if match(t)]


            # For 추천 tabs: shuffle randomly each time
            if main_cat == "all" or sub_cat == "추천" or not sub_cat:
                pool_copy = list(filtered_pool)
                random.shuffle(pool_copy)
                filtered_pool = pool_copy

            start_idx = (page - 1) * limit
            end_idx = start_idx + limit

            results = []
            if start_idx < len(filtered_pool):
                results = filtered_pool[start_idx:min(end_idx, len(filtered_pool))]

            # Fill remaining slots with synthetic threads (only for all or math)
            needed = limit - len(results)
            if needed > 0 and (main_cat == "all" or main_cat == "math") and (not sub_cat or sub_cat == "추천"):
                for i in range(needed):
                    synthetic_idx = (page * limit) + i
                    synth_thread = synthesize_infinite_thread(synthetic_idx)
                    results.append(synth_thread)

            self.send_json_response({
                "page": page,
                "limit": limit,
                "has_more": True,
                "threads": results
            })
            return

        elif path == "/api/likes":
            try:
                self.send_json_response({"threads": get_liked_threads()})
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=503)
            return

        elif path == "/api/categories":
            cat_data = load_categories()
            self.send_json_response(cat_data)
            return

        elif path == "/api/personas":
            self.send_json_response(PERSONA_PROFILES)
            return

        elif path == "/api/export-threads":
            from csv_utils import generate_csv_export
            csv_data = generate_csv_export(ACTIVE_KNOWLEDGE_POOL)
            
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8-sig")
            self.send_header("Content-Disposition", "attachment; filename=\"threadnote_export.csv\"")
            self.end_headers()
            self.wfile.write(b'\xef\xbb\xbf') # UTF-8 BOM for Excel
            self.wfile.write(csv_data.encode("utf-8"))
            return

        elif path in ("/", ""):
            self.path = "/index.html"
            return super().do_GET()
        else:
            return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""

        # ── Single-user server-side likes ──
        if path == "/api/likes":
            try:
                data = json.loads(body.decode("utf-8")) if body else {}
                action = data.get("action", "")
                if action == "like":
                    thread = data.get("thread")
                    if not isinstance(thread, dict):
                        raise ValueError("thread 객체가 필요합니다.")
                    upsert_liked_thread(thread)
                    self.send_json_response({"success": True})
                elif action == "unlike":
                    thread_id = str(data.get("thread_id", "")).strip()
                    if not thread_id:
                        raise ValueError("thread_id가 필요합니다.")
                    delete_liked_thread(thread_id)
                    self.send_json_response({"success": True})
                else:
                    raise ValueError("action은 like 또는 unlike여야 합니다.")
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=503)
            return

        # ── 1. TXT/CSV 스레드 파일 업로드 및 자동 카테고리 추가 ──
        if path == "/api/upload-thread":
            try:
                data = json.loads(body.decode("utf-8"))
                text_content = data.get("text", "")
                filename = data.get("filename", "threads.txt").lower()

                # If base64-encoded file
                file_b64 = data.get("file_base64", "")
                if file_b64:
                    raw = base64.b64decode(file_b64)
                    text_content = raw.decode("utf-8", errors="replace")

                if not text_content.strip():
                    raise ValueError("파일 내용이 비어있습니다.")

                if filename.endswith(".csv"):
                    from csv_utils import parse_thread_csv
                    new_threads = parse_thread_csv(text_content)
                else:
                    new_threads = parse_thread_txt(text_content)
                    
                if not new_threads:
                    raise ValueError("파싱된 스레드가 없습니다. 양식을 확인해주세요.")

                # Auto-create missing categories
                cat_data = load_categories()
                categories_modified = False
                
                for t in new_threads:
                    m_id = t["main_category"]
                    m_label = t["category"]
                    s_label = t["sub_category"]
                    
                    # 1) Add main category if missing
                    existing_main = next((c for c in cat_data["main_categories"] if c["id"] == m_id), None)
                    if not existing_main:
                        cat_data["main_categories"].append({"id": m_id, "label": m_label, "emoji": "📁"})
                        cat_data["sub_categories"][m_id] = []
                        categories_modified = True
                        
                    # 2) Add sub category if missing
                    if s_label and s_label != "추천":
                        subs = cat_data["sub_categories"].get(m_id, [])
                        if s_label not in subs:
                            subs.append(s_label)
                            cat_data["sub_categories"][m_id] = subs
                            categories_modified = True

                if categories_modified:
                    save_categories(cat_data)

                # Overwrite existing threads if Thread ID matches, else prepend
                existing_user = load_user_threads()
                
                for nt in new_threads:
                    # Update in user_threads.json
                    idx = next((i for i, et in enumerate(existing_user) if et["thread_id"] == nt["thread_id"]), -1)
                    if idx >= 0:
                        existing_user[idx] = nt
                    else:
                        existing_user.insert(0, nt)
                        
                    # Update in ACTIVE_KNOWLEDGE_POOL
                    pool_idx = next((i for i, et in enumerate(ACTIVE_KNOWLEDGE_POOL) if et["thread_id"] == nt["thread_id"]), -1)
                    if pool_idx >= 0:
                        ACTIVE_KNOWLEDGE_POOL[pool_idx] = nt
                    else:
                        ACTIVE_KNOWLEDGE_POOL.insert(0, nt)
                        
                save_user_threads(existing_user)

                self.send_json_response({
                    "success": True,
                    "count": len(new_threads),
                    "threads": new_threads,
                    "message": f"✅ {len(new_threads)}개 스레드가 업로드(수정) 되었습니다!"
                })
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=400)

        # ── 2. 소분류 관리 (추가/삭제) ──
        elif path == "/api/likes":
            try:
                self.send_json_response({"threads": get_liked_threads()})
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=503)
            return

        elif path == "/api/categories":
            try:
                data = json.loads(body.decode("utf-8"))
                action = data.get("action", "")
                cat_data = load_categories()
                main_id = data.get("main_id", "")

                if action == "add_sub":
                    sub_name = data.get("sub_name", "").strip()
                    if not sub_name or not main_id:
                        raise ValueError("main_id와 sub_name이 필요합니다.")
                    subs = cat_data["sub_categories"].setdefault(main_id, [])
                    if sub_name not in subs:
                        subs.append(sub_name)
                    save_categories(cat_data)
                    self.send_json_response({"success": True, "sub_categories": cat_data["sub_categories"][main_id]})

                elif action == "remove_sub":
                    sub_name = data.get("sub_name", "").strip()
                    if not sub_name or not main_id:
                        raise ValueError("main_id와 sub_name이 필요합니다.")
                    subs = cat_data["sub_categories"].get(main_id, [])
                    if sub_name in subs:
                        subs.remove(sub_name)
                    save_categories(cat_data)
                    self.send_json_response({"success": True, "sub_categories": subs})

                else:
                    raise ValueError(f"알 수 없는 action: {action}")

            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=400)

        # ── 3. 기존 PDF 업로드 유지 ──
        elif path == "/api/upload":
            try:
                data = json.loads(body.decode("utf-8"))
                filename = data.get("filename", "uploaded_document.pdf")
                file_b64 = data.get("file_base64", "")
                text_content = data.get("text", "")
                persona_id = data.get("persona", "elementary_teacher")

                file_path = os.path.join(UPLOADS_DIR, filename)
                if file_b64:
                    raw_bytes = base64.b64decode(file_b64)
                    with open(file_path, "wb") as f:
                        f.write(raw_bytes)
                    if filename.lower().endswith(".pdf"):
                        extracted = extract_pdf_native(file_path)
                        if extracted:
                            text_content = extracted

                if not text_content:
                    text_content = f"문서 '{filename}'의 핵심 개념과 지도 내용"

                sections = parse_curriculum_sections(text_content)
                if not sections:
                    sections = [{
                        "title": filename.replace(".pdf", ""),
                        "content": text_content.splitlines()[:20],
                        "misconceptions": [],
                        "qna": []
                    }]

                new_threads = []
                for sec in sections[:5]:
                    t = generate_curriculum_thread(sec, persona_id)
                    new_threads.append(t)
                    ACTIVE_KNOWLEDGE_POOL.insert(0, t)

                self.send_json_response({
                    "success": True,
                    "filename": filename,
                    "sections_found": len(sections),
                    "new_threads": new_threads,
                    "message": f"'{filename}'에서 {len(sections)}개 단원을 분석했습니다!"
                })
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=500)

        elif path == "/api/convert-text":
            try:
                data = json.loads(body.decode("utf-8"))
                text = data.get("text", "")
                persona_id = data.get("persona", "elementary_teacher")
                custom_style = data.get("custom_style", "")
                sec = {
                    "title": data.get("title") or text.strip().splitlines()[0][:30],
                    "content": [text],
                    "misconceptions": [l for l in text.splitlines() if "(오)" in l],
                    "qna": [l for l in text.splitlines() if l.startswith("Q.") or l.startswith("Q :")]
                }
                thread = generate_curriculum_thread(sec, persona_id, custom_style)
                ACTIVE_KNOWLEDGE_POOL.insert(0, thread)
                self.send_json_response({"success": True, "thread": thread})
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, status=500)

        else:
            self.send_error(404, "Endpoint not found")


    def send_json_response(self, data, status=200):
        response_bytes = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response_bytes)


class ReusableThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True


def main():
    if DATABASE_URL:
        try:
            init_likes_db()
            print("💾 PostgreSQL 좋아요 저장소 연결 완료")
        except Exception as e:
            print(f"⚠️ PostgreSQL 좋아요 저장소 초기화 실패: {e}")
    else:
        print("ℹ️ DATABASE_URL이 없어 서버 좋아요 저장소가 비활성화되어 있습니다.")

    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
            
    server_address = ("", port)
    httpd = ReusableThreadingServer(server_address, ThreadsCloneHandler)
    print(f"==================================================")
    print(f"🚀 Threads Clone (지식스레드) 서버 가동!")
    print(f"👉 브라우저 주소: http://localhost:{port}")
    print(f"👉 PDF 업로드 & 무한 스크롤(Infinite Scroll) 피드 탑재 완료")
    print(f"==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
        httpd.server_close()


if __name__ == "__main__":
    main()
