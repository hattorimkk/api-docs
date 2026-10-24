#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/exact_186_lines.json') as f:
    items = json.load(f)

print(f"Total lines: {len(items)}")
print("=== CHUNK 2 (lines 60 to 120) ===")
for i, it in enumerate(items[60:120]):
    print(f"--- {i+61} [{it['count']}x] ---\n{it['line']}")

print("\n=== CHUNK 3 (lines 120 to 186) ===")
for i, it in enumerate(items[120:186]):
    print(f"--- {i+121} [{it['count']}x] ---\n{it['line']}")
