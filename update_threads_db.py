#!/usr/bin/env python3
"""
Deep Refactor DB Merger
- Merges refactored thread objects into uploads/user_threads.json by matching thread_id
"""

import json
import os
import sys

THREADS_FILE = "/Users/wang/Documents/threadnote/uploads/user_threads.json"

def merge_refactored_threads(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return 0
        
    with open(filepath, "r", encoding="utf-8") as f:
        new_threads = json.load(f)
        
    if not isinstance(new_threads, list):
        print("Invalid format: expected list of threads")
        return 0
        
    with open(THREADS_FILE, "r", encoding="utf-8") as f:
        db_threads = json.load(f)
        
    # Map by thread_id
    id_map = {t.get("thread_id"): i for i, t in enumerate(db_threads)}
    
    updated_count = 0
    for nt in new_threads:
        tid = nt.get("thread_id")
        if tid in id_map:
            idx = id_map[tid]
            # Update fields
            db_threads[idx]["posts"] = nt.get("posts", db_threads[idx]["posts"])
            db_threads[idx]["tags"] = nt.get("tags", db_threads[idx]["tags"])
            db_threads[idx]["source_insight"] = nt.get("source_insight", db_threads[idx]["source_insight"])
            db_threads[idx]["simulated_comments"] = nt.get("simulated_comments", nt.get("comments", db_threads[idx].get("simulated_comments", [])))
            db_threads[idx]["comments"] = nt.get("comments", nt.get("simulated_comments", db_threads[idx].get("comments", [])))
            if "title" in nt:
                db_threads[idx]["title"] = nt["title"]
            if "sub_category" in nt:
                db_threads[idx]["sub_category"] = nt["sub_category"]
            updated_count += 1
            
    with open(THREADS_FILE, "w", encoding="utf-8") as f:
        json.dump(db_threads, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully merged {updated_count} deeply refactored threads into user_threads.json!")
    return updated_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        merge_refactored_threads(sys.argv[1])
