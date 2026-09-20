import json, sys, os
from app import parse_thread_txt, save_user_threads, load_user_threads

def upload_threads_from_file(filepath):
    if not os.path.exists(filepath):
        print("File not found.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    new_threads = parse_thread_txt(text)
    if not new_threads:
        print("No valid threads found.")
        return
    existing = load_user_threads()
    existing.extend(new_threads)
    save_user_threads(existing)
    print(f"Successfully auto-uploaded {len(new_threads)} threads into the system!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        upload_threads_from_file(sys.argv[1])
