import csv
import io
import re
import random
from datetime import datetime

def generate_csv_export(threads):
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    # Header
    writer.writerow([
        "Thread ID", "대분류(ID)", "대분류(Label)", "소분류", 
        "글쓴이", "아바타", "태그", 
        "훅(Hook)", "핵심(Twist)", "실천(Action)", 
        "댓글(JSON형태)"
    ])
    
    for t in threads:
        tid = t.get("thread_id", "")
        main_id = t.get("main_category", "")
        main_label = t.get("category", "")
        sub_cat = t.get("sub_category", "")
        
        persona = t.get("persona", {})
        author = persona.get("name", "")
        avatar = persona.get("avatar", "")
        
        tags = " ".join(t.get("tags", []))
        
        posts = t.get("posts", [])
        hook, twist, action = "", "", ""
        for p in posts:
            ptype = p.get("type", "").lower()
            text = p.get("text", "")
            if ptype == "hook": hook = text
            elif ptype == "twist": twist = text
            elif ptype == "action": action = text
            else: # If unknown type, append to action or twist
                if not twist: twist = text
                else: action += "\n" + text
                
        comments = []
        for c in t.get("simulated_comments", []):
            comments.append(f"{c.get('avatar','')} {c.get('persona_name','')}: {c.get('text','')}")
        comments_str = "\n".join(comments)
        
        writer.writerow([
            tid, main_id, main_label, sub_cat,
            author, avatar, tags,
            hook, twist, action,
            comments_str
        ])
    return output.getvalue()

def parse_thread_csv(text):
    threads = []
    # Try parsing CSV
    reader = csv.DictReader(io.StringIO(text.strip()))
    for row in reader:
        # Check if basic fields exist
        if not row.get("대분류(Label)"): continue
        
        main_id = row.get("대분류(ID)", "").strip()
        main_label = row.get("대분류(Label)", "").strip()
        sub_label = row.get("소분류", "").strip()
        author_name = row.get("글쓴이", "익명 선생님").strip()
        avatar = row.get("아바타", "📝").strip()
        tags_raw = row.get("태그", "").strip()
        tags = tags_raw.split() if tags_raw else []
        
        hook = row.get("훅(Hook)", "").strip()
        twist = row.get("핵심(Twist)", "").strip()
        action = row.get("실천(Action)", "").strip()
        comments_str = row.get("댓글(JSON형태)", "").strip()
        
        thread_posts = []
        if hook: thread_posts.append({"type": "hook", "text": hook})
        if twist: thread_posts.append({"type": "twist", "text": twist})
        if action: thread_posts.append({"type": "action", "text": action})
        
        comments = []
        for c_line in comments_str.splitlines():
            cm = re.match(r'^(.+?)\s+(.+?):\s*(.+)$', c_line.strip())
            if cm:
                comments.append({
                    "avatar": cm.group(1).strip(),
                    "persona_name": cm.group(2).strip(),
                    "text": cm.group(3).strip()
                })
        
        # If no main_id is provided, guess it
        if not main_id:
            main_id_map = {
                "국어": "korean", "수학": "math", "영어": "english",
                "사회": "social", "과학": "science", "음악": "music",
                "총론": "general", "미술": "art", "실과": "tech",
                "통합": "integrated", "체육": "pe", "도덕": "moral", "창체": "creative"
            }
            main_id = main_id_map.get(main_label, "math")
            
        tid = row.get("Thread ID", "").strip()
        if not tid:
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
                "title": sub_label or main_label,
                "grade": "",
                "academic_quote": "",
                "curriculum_code": ""
            },
            "simulated_comments": comments
        }
        threads.append(thread)
    return threads
