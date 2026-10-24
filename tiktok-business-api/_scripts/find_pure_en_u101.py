#!/usr/bin/env python3
import os, sys, re
from collections import Counter

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
from inspect_remaining_u101 import new_text

parts = new_text.split('```')
prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
pure_en_lines = []
for l in prose.splitlines():
    ls = l.strip()
    if not ls or ls.startswith('<a id=') or ls.startswith('<!-- doc_id:'):
        continue
    if not vi_re.search(ls):
        words = re.findall(r'\b[A-Za-z]{3,}\b', ls)
        if len(words) >= 4:
            pure_en_lines.append(ls)

counts = Counter(pure_en_lines)
print('Total pure English lines (no Vietnamese characters at all):', len(pure_en_lines))
print('Unique pure English lines:', len(counts))
print('Top 50 pure English lines:')
for l, c in counts.most_common(50):
    print(f'{c:3d}: {l[:110]}')

with open(os.path.join(os.path.dirname(_SCRIPT_DIR), '_work/u101_pure_en.txt'), 'w', encoding='utf-8') as f:
    for l, c in counts.most_common():
        f.write(f"{c:4d}\t{l}\n")
