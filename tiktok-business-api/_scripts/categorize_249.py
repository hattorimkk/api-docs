#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/final_untrans_lines.json') as f:
    items = json.load(f)

table_rows = []
headings = []
bullets = []
plain = []

for it in items:
    l = it['line']
    if l.startswith('|'):
        table_rows.append(it)
    elif l.startswith('#'):
        headings.append(it)
    elif l.startswith(('-', '•', '*', '1.', '2.', '3.', '4.', '5.', '6.')):
        bullets.append(it)
    else:
        plain.append(it)

print(f"Table rows: {len(table_rows)}")
print(f"Headings: {len(headings)}")
print(f"Bullets / Numbers: {len(bullets)}")
print(f"Plain prose: {len(plain)}")
