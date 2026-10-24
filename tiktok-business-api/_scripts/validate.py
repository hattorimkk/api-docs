#!/usr/bin/env python3
"""Kiểm tra đầu ra dịch so với nguồn.
Dùng:  python3 _scripts/validate.py [unit_id ...]   (mặc định: tất cả unit đã có file)
Kiểm tra: file tồn tại; mỗi doc_id có marker; tên field (cột đầu của bảng nguồn) xuất hiện trong bản dịch;
code fence cân bằng; tỉ lệ độ dài hợp lý.
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
units = json.load(open(os.path.join(ROOT, "_work", "units.json"), encoding="utf-8"))
want = set(sys.argv[1:])
FIELD_RE = re.compile(r"(?m)^\| (?:↳+ )?([A-Za-z_][A-Za-z0-9_\-\.\[\]]*)\b[^|]*\|")


def fields_of(doc_id):
    src = open(os.path.join(ROOT, "_clean", f"{doc_id}.md"), encoding="utf-8").read()
    fs = set()
    for m in FIELD_RE.finditer(src):
        f = m.group(1)
        if f.lower() in ("field", "name", "value", "parameter", "enum", "description", "type"):
            continue
        fs.add(f)
    return fs


tot_missing = 0
rows = []
for u in units:
    if want and u["unit_id"] not in want:
        continue
    path = os.path.join(ROOT, u["out"])
    if not os.path.exists(path):
        if want:
            rows.append((u["unit_id"], "THIẾU FILE", u["out"]))
        continue
    txt = open(path, encoding="utf-8").read()
    issues = []
    if txt.count("```") % 2:
        issues.append("code fence lẻ (file có thể bị cắt)")
    miss_docs = [d for d in u["doc_ids"] if f"doc_id: {d}" not in txt]
    if miss_docs:
        issues.append(f"thiếu {len(miss_docs)}/{len(u['doc_ids'])} doc_id: {miss_docs[:5]}")
    if u["mode"] == "full":
        miss_fields = {}
        for d in u["doc_ids"]:
            if d in miss_docs:
                continue
            for f in fields_of(d):
                if f"`{f}`" not in txt and f not in txt:
                    miss_fields.setdefault(d, []).append(f)
        nm = sum(len(v) for v in miss_fields.values())
        if nm:
            issues.append(f"thiếu {nm} tên field, ví dụ: " + "; ".join(f"{d}:{v[:6]}" for d, v in list(miss_fields.items())[:3]))
            tot_missing += nm
        ratio = len(txt) / max(1, u["chars"])
        if ratio < 0.35:
            issues.append(f"bản dịch quá ngắn so với nguồn (tỉ lệ {ratio:.2f})")
    if re.search(r"\(doc:\d+\)", txt) is None and u["mode"] == "full" and u["chars"] > 5000:
        pass
    rows.append((u["unit_id"], "OK" if not issues else "VẤN ĐỀ", u["out"] + ("  -> " + " | ".join(issues) if issues else "")))

for r in rows:
    print(*r)
print("tổng field thiếu:", tot_missing)

