#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

items.sort(key=lambda x: x['count'], reverse=True)

print("--- TOP 40 ITEMS IN unique_outside_table_mixed ---")
for i, it in enumerate(items[:40]):
    print(f"{i+1}. [{it['count']:2d}x] {it['line'][:110]}")
