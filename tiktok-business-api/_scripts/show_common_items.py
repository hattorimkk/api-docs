#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/categorized_untranslated.json') as f:
    cat = json.load(f)

common = cat['other_or_common']
common.sort(key=lambda x: x['count'], reverse=True)

print("=== TOP 40 MULTI-CLUSTER / COMMON ITEMS ===")
for it in common[:40]:
    print(f"[{it['count']:2d}x] {it['orig']}")
