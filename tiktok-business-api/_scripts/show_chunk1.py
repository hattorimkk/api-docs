#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/exact_186_lines.json') as f:
    items = json.load(f)

print(f"Total lines: {len(items)}")
for i, it in enumerate(items[:60]):
    print(f"--- {i+1} [{it['count']}x] ---\n{it['line']}")
