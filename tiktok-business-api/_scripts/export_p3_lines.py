#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/residual_p3.json') as f:
    items = json.load(f)

print(f"Total items in residual_p3: {len(items)}")

with open('tiktok-business-api/_work/p3_lines_to_trans.txt', 'w', encoding='utf-8') as f:
    for it in items:
        f.write(f"DOC: {it['doc_id']}\nORIG: {it['line']}\n\n")

print("Saved to tiktok-business-api/_work/p3_lines_to_trans.txt")
