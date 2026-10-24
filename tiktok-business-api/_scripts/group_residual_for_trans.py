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

with open('tiktok-business-api/_work/residual_short_labels.json') as f:
    short_labels = json.load(f)

with open('tiktok-business-api/_work/residual_links.json') as f:
    links = json.load(f)

# Dump grouped json
grouped = {
    "short_labels": short_labels,
    "links": links,
    "table_rows": [it for it in items if it['line'].startswith('|')],
    "doc_sentences": {}
}

non_tables = [it for it in items if not it['line'].startswith('|')]
for it in non_tables:
    line = it['line']
    found = "multi_or_unmapped"
    for did, dtext in doc_map.items():
        if line in dtext:
            found = did
            break
    if found not in grouped["doc_sentences"]:
        grouped["doc_sentences"][found] = []
    grouped["doc_sentences"][found].append(it)

with open('tiktok-business-api/_work/residual_grouped_for_trans.json', 'w', encoding='utf-8') as f:
    json.dump(grouped, f, ensure_ascii=False, indent=2)

print("Saved grouped residual items.")
print(f"Short labels: {len(grouped['short_labels'])}")
print(f"Links: {len(grouped['links'])}")
print(f"Table rows: {len(grouped['table_rows'])}")
print(f"Docs count: {len(grouped['doc_sentences'])}")
