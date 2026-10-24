#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/residual_grouped_for_trans.json') as f:
    g = json.load(f)

ds = g['doc_sentences']
all_sentences = []
for did, items in ds.items():
    for it in items:
        all_sentences.append({"doc_id": did, "line": it['line'], "count": it['count']})

print(f"Total non-table sentences: {len(all_sentences)}")

# Let's save them as a clean list of unique lines
unique_lines = list({s['line']: s for s in all_sentences}.values())
print(f"Unique non-table sentence lines: {len(unique_lines)}")

with open('tiktok-business-api/_work/all_residual_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(unique_lines, f, ensure_ascii=False, indent=2)
