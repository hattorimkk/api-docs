#!/usr/bin/env python3
import json, re
from collections import Counter

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

# Sort by count descending
items.sort(key=lambda x: x['count'], reverse=True)

# Group lines by their first 3-5 words
prefix_counts = Counter()
for it in items:
    words = it['line'].split()[:4]
    prefix = ' '.join(words)
    prefix_counts[prefix] += it['count']

print("--- TOP 35 LINE PREFIXES ---")
for pref, total_cnt in prefix_counts.most_common(35):
    print(f"[{total_cnt:3d}x] {repr(pref)}")
