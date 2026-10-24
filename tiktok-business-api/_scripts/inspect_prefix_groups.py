#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

prefixes = [
    'Một trong các giá', 'Một trong các loại', 'Một trong các tùy',
    'Đã tắt hoặc đã', 'Bật hoặc tắt (Enabled', 'Not specified or specify',
    'Specify a valid value', 'Disable or enabled with'
]

grouped = {p: [] for p in prefixes}
grouped['other'] = []

for it in items:
    matched = False
    for p in prefixes:
        if it['line'].startswith(p):
            grouped[p].append(it)
            matched = True
            break
    if not matched:
        grouped['other'].append(it)

for p in prefixes:
    print(f"=== Prefix: {p} ({len(grouped[p])} items, total count: {sum(x['count'] for x in grouped[p])}) ===")
    for it in grouped[p][:5]:
        print(f"  [{it['count']}x] {it['line'][:110]}")

print(f"\nRemaining in other: {len(grouped['other'])} items, total count: {sum(x['count'] for x in grouped['other'])}")
