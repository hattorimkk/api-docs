#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

docs = re.split(r'(?=<a id="doc-\d+"></a>)', text)
doc_map = {}
for d in docs:
    m = re.search(r'<a id="doc-(\d+)"></a>', d)
    if m:
        doc_map[m.group(1)] = d

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

print(f"Total unique mixed lines: {len(items)}")

# Check how many lines appear in each doc
doc_counts = {}
for it in items:
    l = it['line']
    for did, dtext in doc_map.items():
        if l in dtext:
            doc_counts[did] = doc_counts.get(did, 0) + 1

print(f"Number of docs containing mixed lines: {len(doc_counts)}")
for did, cnt in sorted(doc_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"Doc {did}: {cnt} lines")
