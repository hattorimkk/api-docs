#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/final_untrans_lines.json') as f:
    items = json.load(f)

print(f"Total remaining lines: {len(items)}")

with open('tiktok-business-api/_work/all_249_untrans_lines.txt', 'w', encoding='utf-8') as f:
    for i, it in enumerate(items):
        f.write(f"--- LINE {i+1} (cnt: {it['count']}) ---\n{it['line']}\n\n")

print("Saved all 249 lines to tiktok-business-api/_work/all_249_untrans_lines.txt")
