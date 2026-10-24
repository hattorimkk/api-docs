#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

print(f"Total unique lines: {len(items)}")

# Let's inspect by category
toc_lines = []
param_desc_lines = [] # line starting with • or containing parameter guidance
setting_val_lines = [] # e.g. "Một trong các loại sau: ..."
intro_lines = []
other_lines = []

for it in items:
    l = it['line']
    if l.startswith('- [') and 'doc-' in l:
        toc_lines.append(it)
    elif '• When you select a campaign budget mode' in l or '• When budget_optimize_on' in l:
        param_desc_lines.append(it)
    elif l.startswith('Một trong các') or l.startswith('Bật hoặc tắt') or l.startswith('Đã tắt'):
        setting_val_lines.append(it)
    elif 'With the' in l or 'objective allows you to' in l or 'is a type of' in l:
        intro_lines.append(it)
    else:
        other_lines.append(it)

print(f"TOC lines: {len(toc_lines)}")
print(f"Setting val lines: {len(setting_val_lines)}")
print(f"Intro lines: {len(intro_lines)}")
print(f"Budget/Schedule lines: {len(param_desc_lines)}")
print(f"Other lines: {len(other_lines)}")
