#!/usr/bin/env python3
import os, sys, re
from collections import defaultdict

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/original_en_blocks.txt"), "r", encoding="utf-8") as f:
    blocks = [line.strip().split('\t', 1) for line in f if '\t' in line]

cats = defaultdict(list)
for cnt_s, block in blocks:
    cnt = int(cnt_s)
    b = block.replace(' ⏎ ', '\n').strip()
    if b.startswith('#'):
        cats['heading'].append((cnt, b))
    elif b.startswith('>'):
        cats['callout_or_breadcrumb'].append((cnt, b))
    elif b.startswith('|'):
        cats['table_row'].append((cnt, b))
    elif b.startswith('- ') or b.startswith('• ') or re.match(r'^\d+\.', b):
        cats['bullet_or_step'].append((cnt, b))
    elif '\n' in b:
        cats['multiline_block'].append((cnt, b))
    else:
        cats['single_line'].append((cnt, b))

for cat, items in sorted(cats.items(), key=lambda x: sum(c for c, _ in x[1]), reverse=True):
    total = sum(c for c, _ in items)
    print(f"{cat}: {len(items)} unique blocks, {total} total occurrences")
