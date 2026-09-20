#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lightweight Local Integrity Daemon for ThreadNote DB
- Runs continuously in the background
- Zero API token consumption
- Continuously audits all 2,392 threads in uploads/user_threads.json
- Logs status to scratch/daemon_status.log
"""

import json
import time
import os
import re

DB_PATH = "/Users/wang/Documents/threadnote/uploads/user_threads.json"
LOG_PATH = "/Users/wang/Documents/threadnote/scratch/daemon_status.log"

def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)

def audit_and_optimize():
    if not os.path.exists(DB_PATH):
        log(f"Error: {DB_PATH} does not exist.")
        return

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            db = json.load(f)
    except Exception as e:
        log(f"Error reading DB: {e}")
        return

    total = len(db)
    cleaned_posts = 0

    for t in db:
        for p in t.get("posts", []):
            text = p.get("text", "")
            # Ensure no emoji list spam
            new_text = re.sub(r'(\*\*|\b)?[1-9]️⃣[ \t]*', r'\1', text)
            new_text = re.sub(r'(\*\*|\b)?🔟[ \t]*', r'\1', new_text)
            new_text = re.sub(r'(\*\*|\b)?[📍⭕👉▶️➗▪️▫️■□][ \t]*', r'\1', new_text)
            # Ensure unicode math
            new_text = new_text.replace(r'\times', '×').replace(r'\div', '÷')
            if new_text != text:
                p["text"] = new_text.strip()
                cleaned_posts += 1

    if cleaned_posts > 0:
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        log(f"Audit cycle: Cleaned {cleaned_posts} post texts. Total threads verified: {total}")
    else:
        log(f"Audit cycle: 100% Clean. Total threads verified: {total}")

if __name__ == "__main__":
    log("ThreadNote Local Integrity Daemon Started (Token-Zero Architecture)")
    while True:
        try:
            audit_and_optimize()
        except Exception as e:
            log(f"Daemon exception: {e}")
        time.sleep(300)
