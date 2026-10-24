#!/usr/bin/env python3
import json, re
from collections import Counter

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split('```')
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
all_prose_lines = []
for p in prose_parts:
    all_prose_lines.extend(p.splitlines())

non_empty = [l.strip() for l in all_prose_lines if l.strip()]
content_lines = [l for l in non_empty if not (l.startswith('<a id=') or l.startswith('<!-- doc_id:'))]

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
vi_lines = [l for l in content_lines if vi_re.search(l)]

# Find english clauses (3 or more consecutive ascii words)
mixed = []
for l in vi_lines:
    matches = re.findall(r'\b[A-Za-z]{3,}(?:\s+[A-Za-z]{3,}){2,}\b', l)
    filtered = []
    for m in matches:
        words = [w.lower() for w in m.split()]
        if all(w in {'smart', 'campaign', 'campaigns', 'tiktok', 'ads', 'manager', 'business', 'api', 'o2o', 'gmv', 'max', 'vsa', 'catalog', 'instant', 'page', 'form'} for w in words):
            continue
        filtered.append(m)
    if filtered:
        mixed.append((l, filtered))

print(f"Total vi_lines with English clauses: {len(mixed)} (unique: {len(set(l for l, _ in mixed))})")

data = [{"line": l, "clauses": f} for l, f in Counter(l for l, _ in mixed).most_common()]
with open('tiktok-business-api/_work/mixed_vi_lines.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Top 20 mixed lines:")
for d in data[:20]:
    print(f"MIXED: {d['line'][:110]}")
