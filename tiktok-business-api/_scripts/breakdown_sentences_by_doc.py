#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    full_text = f.read()

docs = re.split(r'(?=<a id="doc-\d+"></a>)', full_text)
doc_map = {}
for d in docs:
    m = re.search(r'<a id="doc-(\d+)"></a>', d)
    if m:
        did = m.group(1)
        doc_map[did] = d

with open('tiktok-business-api/_work/real_prose_sentences.json') as f:
    items = json.load(f)

non_tables = [it for it in items if not it['line'].startswith('|')]

doc_sentence_counts = {}
for it in non_tables:
    line = it['line']
    found_dids = []
    for did, dtext in doc_map.items():
        if line in dtext:
            found_dids.append(did)
    key = tuple(found_dids)
    doc_sentence_counts[key] = doc_sentence_counts.get(key, 0) + 1

print(f"Total non-table sentence entries: {len(non_tables)}")
print(f"Breakdown by Doc IDs:")
for k, cnt in sorted(doc_sentence_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"  Docs {k}: {cnt} sentences")
