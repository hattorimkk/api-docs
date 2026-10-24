#!/usr/bin/env python3
import os, sys, re
from collections import Counter

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
from inspect_remaining_u101 import new_text

parts = new_text.split('```')
prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
mixed_lines = []
for l in prose.splitlines():
    ls = l.strip()
    if not ls or ls.startswith('<a id=') or ls.startswith('<!-- doc_id:') or ls.startswith('| Thiết lập (Setting)'):
        continue
    if vi_re.search(ls):
        # Has Vietnamese, but check if it has English clauses / phrases (e.g. 4+ consecutive English words)
        en_matches = re.findall(r'\b[A-Za-z]{3,}(?:\s+[A-Za-z]{3,}){2,}\b', ls)
        # Filter technical terms like "Smart+ Campaign", "TikTok Ads Manager", etc.
        filtered = []
        for em in en_matches:
            # ignore if just allowed brand names
            words = [w.lower() for w in em.split()]
            if all(w in {'smart', 'campaign', 'campaigns', 'tiktok', 'ads', 'manager', 'business', 'api', 'o2o', 'gmv', 'max', 'vsa', 'catalog', 'instant', 'page', 'form'} for w in words):
                continue
            filtered.append(em)
        if filtered:
            mixed_lines.append(ls)

counts = Counter(mixed_lines)
print('Total mixed lines with English clauses:', len(mixed_lines))
print('Unique mixed lines:', len(counts))
print('Top 30 mixed lines:')
for l, c in counts.most_common(30):
    print(f'{c:3d}: {l[:110]}')

with open(os.path.join(os.path.dirname(_SCRIPT_DIR), '_work/u101_mixed_en.txt'), 'w', encoding='utf-8') as f:
    for l, c in counts.most_common():
        f.write(f"{c:4d}\t{l}\n")
