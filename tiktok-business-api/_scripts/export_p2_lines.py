#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/residual_p2.json') as f:
    items = json.load(f)

print(f"Total items in residual_p2: {len(items)}")

# Let's write out each line to a file so we can generate the translation dictionary
with open('tiktok-business-api/_work/p2_lines_to_trans.txt', 'w', encoding='utf-8') as f:
    for it in items:
        f.write(f"DOC: {it['doc_id']}\nORIG: {it['line']}\n\n")

print("Saved to tiktok-business-api/_work/p2_lines_to_trans.txt")
