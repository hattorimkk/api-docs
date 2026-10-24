#!/usr/bin/env python3
import json, re
from collections import Counter

with open('tiktok-business-api/_work/outside_table_mixed.txt') as f:
    lines = f.readlines()

print(f"Total outside table mixed lines: {len(lines)}")

# Extract pure string
raw_lines = [re.sub(r'^\[\d+ en words\]\s*', '', l).strip() for l in lines]
c = Counter(raw_lines)

print(f"Unique lines: {len(c)}")
print("\n--- TOP 30 UNIQUE MIXED OUTSIDE TABLE LINES BY FREQUENCY ---")
for l, cnt in c.most_common(30):
    print(f"[{cnt:2d}x] {l[:110]}")

with open('tiktok-business-api/_work/unique_outside_table_mixed.json', 'w', encoding='utf-8') as f:
    json.dump([{"line": l, "count": cnt} for l, cnt in c.most_common()], f, ensure_ascii=False, indent=2)
