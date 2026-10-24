#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

cluster3_ids = [
    '1741942179356738', '1837161048383489', '1741942291730434', '1750361698613249',
    '1774519076905985', '1775099621140482', '1782087855154177', '1750361719059457',
    '1759232259360770', '1754162402455554', '1785886237030401', '1754726939130882',
    '1742003478618114'
]

for did in cluster3_ids:
    pattern = rf'(<a id="doc-{did}"></a>[\s\S]*?)(?=<a id="doc-\d+"></a>|$)'
    m = re.search(pattern, text)
    if m:
        sec = m.group(1)
        parts = sec.split('```')
        prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])
        print(f"=== DOC {did} ===")
        for line in prose.splitlines()[:15]:
            if line.strip():
                print("  ", line[:100])
