#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/all_1501_en_lines.json') as f:
    data = json.load(f)

for item in data[50:100]:
    cnt = item['count']
    l = item['line']
    print(f"{cnt:3d}: {l}")
