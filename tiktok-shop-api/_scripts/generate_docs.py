#!/usr/bin/env python3
"""
Script biên soạn và chuẩn hóa tài liệu Tiếng Việt cho các phân hệ của TikTok Shop Partner API.
Tổng hợp dữ liệu từ _raw/docs/, phân loại theo 19 danh mục chuyên sâu và tạo các file docs/<category>/README.md.
"""
import os
import json
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW_DOCS = os.path.join(ROOT, "_raw", "docs")
INDEX_PATH = os.path.join(ROOT, "_raw", "index.json")
DOCS_DIR = os.path.join(ROOT, "docs")

os.makedirs(DOCS_DIR, exist_ok=True)

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index = json.load(f)

doc_map = {x["document_id"]: x for x in index}

def clean_content(raw_text):
    if not raw_text:
        return ""
    # Loại bỏ base64 svg rườm rà
    cleaned = re.sub(r'data:image/svg\+xml;base64,[a-zA-Z0-9+/=]+', '[DIAGRAM_SVG]', raw_text)
    return cleaned

def parse_api_doc(raw_json):
    content = raw_json.get("content", "")
    lines = content.splitlines()
    
    path = ""
    method = ""
    desc_lines = []
    mode = "init"
    
    for line in lines:
        if line.startswith("# Path:"):
            path = line.replace("# Path:", "").strip()
        elif line.startswith("# Method:"):
            method = line.replace("# Method:", "").replace("[", "").replace("]", "").strip()
        elif line.startswith("# Function Description"):
            mode = "desc"
            continue
        elif line.startswith("# ") and mode == "desc":
            mode = "other"
        
        if mode == "desc":
            desc_lines.append(line)
            
    desc = "\n".join(desc_lines).strip()
    return {
        "title": raw_json.get("title", ""),
        "path": path,
        "method": method,
        "desc": desc,
        "raw_content": content
    }

print("Khởi tạo hoàn tất generator script.")

