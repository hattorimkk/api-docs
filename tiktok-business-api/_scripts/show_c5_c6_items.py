#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/categorized_untranslated.json') as f:
    cat = json.load(f)

c5 = cat['c5']
print(f"=== Total C5 items: {len(c5)} ===")
for i, it in enumerate(c5):
    print(f"{i+1}. [{it['count']}x] {it['orig'][:100]}")

c6 = cat['c6']
print(f"\n=== Total C6 items: {len(c6)} ===")
for i, it in enumerate(c6):
    print(f"{i+1}. [{it['count']}x] {it['orig'][:100]}")
