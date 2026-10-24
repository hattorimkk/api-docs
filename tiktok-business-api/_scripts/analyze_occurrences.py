#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

# Sort by count
items.sort(key=lambda x: x['count'], reverse=True)

# Top 50 lines account for how many occurrences?
top50_occ = sum(x['count'] for x in items[:50])
top100_occ = sum(x['count'] for x in items[:100])
top200_occ = sum(x['count'] for x in items[:200])
total_occ = sum(x['count'] for x in items)

print(f"Top 50 unique lines account for: {top50_occ} / {total_occ} occurrences ({top50_occ/total_occ*100:.1f}%)")
print(f"Top 100 unique lines account for: {top100_occ} / {total_occ} occurrences ({top100_occ/total_occ*100:.1f}%)")
print(f"Top 200 unique lines account for: {top200_occ} / {total_occ} occurrences ({top200_occ/total_occ*100:.1f}%)")
