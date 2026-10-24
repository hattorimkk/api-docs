#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/untouched_after_c3.json') as f:
    items = json.load(f)

print(f"Total untouched: {len(items)}")
# Sort by count descending
items.sort(key=lambda x: x['count'], reverse=True)

print("\n--- TOP 30 UNTOUCHED BY FREQUENCY ---")
for it in items[:30]:
    print(f"[{it['count']:2d}x] {it['orig'][:100]}")

print("\n--- SAMPLE OF UNTOUCHED WITH COUNT == 1 ---")
singletons = [it for it in items if it['count'] == 1]
print(f"Total singletons: {len(singletons)}")
for it in singletons[:20]:
    print(f"     {it['orig'][:100]}")
