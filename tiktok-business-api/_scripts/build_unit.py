#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
units_file = os.path.join(ROOT, "_work", "units.json")
with open(units_file, "r", encoding="utf-8") as f:
    units = json.load(f)

unit_map = {u["unit_id"]: u for u in units}


def build_unit(unit_id):
    if unit_id not in unit_map:
        print(f"Unknown unit_id: {unit_id}")
        return False
    u = unit_map[unit_id]
    target_path = os.path.join(ROOT, u["out"])
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    title_vi = u.get("title_vi", "Tài liệu API")
    key = u.get("key", "API Reference")
    mode = u.get("mode", "full")

    header = f"# {title_vi}\n\n"
    header += f"> Phân hệ: {key}.\n"
    header += "> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.\n\n---\n\n"
    header += "## Mục lục điều hướng\n"

    toc_items = []
    doc_sections = []

    for idx, doc_id in enumerate(u["doc_ids"], 1):
        clean_file = os.path.join(ROOT, "_clean", f"{doc_id}.md")
        if not os.path.exists(clean_file):
            continue
        with open(clean_file, "r", encoding="utf-8") as f:
            src = f.read()

        doc_title = f"Tài liệu {idx}"
        for l in src.splitlines():
            if l.startswith("# "):
                doc_title = l.replace("# ", "").strip()
                break

        anchor = f"doc-{doc_id}"
        toc_items.append(f"- [{idx}. {doc_title} (doc:{doc_id})](#{anchor})")

        lines = src.splitlines()
        clean_lines = []
        for l in lines:
            if l.startswith("``` xtable"):
                continue
            if l.strip() == "```" and len(clean_lines) > 0 and "|" in clean_lines[-1]:
                continue
            clean_l = l
            if clean_l.startswith("|"):
                clean_l = re.sub(r"\{[0-9]+%\}", "", clean_l)
                clean_l = re.sub(r"\{Required\}", "*(Required)*", clean_l)
                clean_l = re.sub(r"\{Conditional\}", "*(Conditional)*", clean_l)
                clean_l = re.sub(r"\{\+Conditional\}", "*(Conditional)*", clean_l)
            clean_lines.append(clean_l)

        doc_text = "\n".join(clean_lines)
        if doc_text.count("```") % 2 != 0:
            doc_text += "\n```\n"

        doc_sections.append(f'<a id="{anchor}"></a>\n<!-- doc_id: {doc_id} -->\n' + doc_text)

    toc_str = "\n".join(toc_items) + "\n\n---\n\n"

    practical_code = f"""
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **{title_vi}**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {{
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}}

def execute_request():
    url = f"{{BASE_URL}}/example/get/"
    params = {{"advertiser_id": ADVERTISER_ID}}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {{data.get('code')}} - {{data.get('message')}}")
        return None

if __name__ == "__main__":
    execute_request()
```
"""

    full_content = header + toc_str + "\n\n---\n\n".join(doc_sections) + practical_code + "\n"

    # Ensure even number of code fences
    if full_content.count("```") % 2 != 0:
        full_content += "\n```\n"

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    res = subprocess.run(
        ["python3", os.path.join(ROOT, "_scripts", "validate.py"), unit_id], capture_output=True, text=True
    ).stdout
    print(res.strip())
    return " OK " in res


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 _scripts/build_unit.py <unit_id> [unit_id ...]")
        sys.exit(1)
    for uid in args:
        build_unit(uid)

