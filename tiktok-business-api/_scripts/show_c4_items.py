#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/categorized_untranslated.json') as f:
    cat = json.load(f)

c4 = cat['c4']
print(f"Total C4 items: {len(c4)}")
for i, it in enumerate(c4):
    print(f"{i+1}. [{it['count']}x] {it['orig']}")
