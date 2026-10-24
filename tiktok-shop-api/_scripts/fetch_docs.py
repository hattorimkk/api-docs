#!/usr/bin/env python3
"""
Tải toàn bộ tài liệu và API endpoint của TikTok Shop Partner API v2 về thư mục _raw/docs/.
Endpoint: https://partner.tiktokshop.com/api/v1/document/detail?document_id={doc_id}&workspace_id=3
Tài liệu đã tải sẽ tự động được bỏ qua (resume-friendly).
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://partner.tiktokshop.com/api/v1/document/detail"
WORKSPACE_ID = "3"
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_raw")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
INDEX_FILE = os.path.join(ROOT_DIR, "index.json")

os.makedirs(DOCS_DIR, exist_ok=True)

def fetch_single_doc(doc_info, retries=4):
    doc_id = doc_info["document_id"]
    out_path = os.path.join(DOCS_DIR, f"{doc_id}.json")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 30:
        return doc_id, "skip", doc_info["title"]

    url = f"{BASE_URL}?document_id={doc_id}&workspace_id={WORKSPACE_ID}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }

    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("code") == 0:
                    with open(out_path, "w", encoding="utf-8") as f:
                        json.dump(data.get("data", {}), f, ensure_ascii=False, indent=2)
                    return doc_id, "ok", doc_info["title"]
                else:
                    return doc_id, f"ERR_{data.get('code')}: {data.get('message')}", doc_info["title"]
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (attempt + 1))

    return doc_id, f"EXC: {last_err}", doc_info["title"]

def main():
    if not os.path.exists(INDEX_FILE):
        print(f"Error: {INDEX_FILE} not found!")
        sys.exit(1)

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        items = json.load(f)

    # Chỉ tải các document lá (không phải thư mục)
    targets = [x for x in items if not x.get("is_dir")]
    print(f"Tổng số tài liệu cần kiểm tra/tải: {len(targets)}")

    done = 0
    errors = 0
    skipped = 0

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(fetch_single_doc, t) for t in targets]
        for f in as_completed(futures):
            doc_id, status, title = f.result()
            done += 1
            if status == "skip":
                skipped += 1
            elif status == "ok":
                pass
            else:
                errors += 1
                print(f"[{status}] {title} ({doc_id})")

            if done % 100 == 0 or done == len(targets):
                print(f"Tiến độ: {done}/{len(targets)} (Mới tải: {done - skipped - errors}, Bỏ qua: {skipped}, Lỗi: {errors})", flush=True)

    print(f"Hoàn thành! Tổng: {done}, Mới tải: {done - skipped - errors}, Bỏ qua: {skipped}, Lỗi: {errors}")

if __name__ == "__main__":
    main()

