#!/usr/bin/env python3
import os, sys, re
from collections import defaultdict

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)

pure_file = os.path.join(os.path.dirname(_SCRIPT_DIR), '_work/u101_pure_en.txt')
mixed_file = os.path.join(os.path.dirname(_SCRIPT_DIR), '_work/u101_mixed_en.txt')

all_lines = []
for fpath in [pure_file, mixed_file]:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('\t', 1)
                if len(parts) == 2:
                    cnt = int(parts[0])
                    txt = parts[1]
                    all_lines.append((cnt, txt))

print(f"Loaded {len(all_lines)} lines.")

# Group by category
categories = defaultdict(list)
for cnt, txt in all_lines:
    t = txt.strip()
    if t.startswith('|') and t.endswith('|'):
        categories['table_row'].append((cnt, t))
    elif t.startswith('>'):
        categories['quote_note'].append((cnt, t))
    elif t.startswith('•') or t.startswith('- ') or re.match(r'^\d+\.', t):
        categories['bullet_or_step'].append((cnt, t))
    elif t.startswith('Any of the following') or t.startswith('Một trong các'):
        categories['enum_options'].append((cnt, t))
    elif 'Note:' in t or 'Lưu ý:' in t:
        categories['has_note'].append((cnt, t))
    elif 'To learn more' in t or 'Để tìm hiểu' in t:
        categories['learn_more'].append((cnt, t))
    elif t.startswith('When ') or t.startswith('Khi '):
        categories['condition_when'].append((cnt, t))
    elif t.startswith('Specify ') or t.startswith('Pass ') or t.startswith('Do not '):
        categories['instructions'].append((cnt, t))
    else:
        categories['other_prose'].append((cnt, t))

for cat, items in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    total_occurrences = sum(c for c, _ in items)
    print(f"Category '{cat}': {len(items)} unique ({total_occurrences} occurrences)")
