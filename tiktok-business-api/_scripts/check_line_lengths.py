#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

short_lines = [it for it in items if len(it['line'].split()) <= 15]
long_lines = [it for it in items if len(it['line'].split()) > 15]

print(f"Total lines: {len(items)}")
print(f"Short lines (<= 15 words): {len(short_lines)} (total occurrences: {sum(x['count'] for x in short_lines)})")
print(f"Long lines (> 15 words): {len(long_lines)} (total occurrences: {sum(x['count'] for x in long_lines)})")
