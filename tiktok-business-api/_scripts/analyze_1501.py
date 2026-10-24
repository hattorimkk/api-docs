#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/all_1501_en_lines.json') as f:
    data = json.load(f)

c_ge_5 = [d for d in data if d['count'] >= 5]
c_2_to_4 = [d for d in data if 2 <= d['count'] < 5]
c_1 = [d for d in data if d['count'] == 1]

print(f"Count >= 5: {len(c_ge_5)} lines, sum occurrences: {sum(d['count'] for d in c_ge_5)}")
print(f"Count 2-4: {len(c_2_to_4)} lines, sum occurrences: {sum(d['count'] for d in c_2_to_4)}")
print(f"Count == 1: {len(c_1)} lines, sum occurrences: {len(c_1)}")
