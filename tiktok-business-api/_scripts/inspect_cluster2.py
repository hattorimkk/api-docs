#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

cluster2_ids = [
    '1739470742024193', '1774482920012801', '1774482976097281', '1827752507854850',
    '1829635758164994', '1774482992153601', '1774482999036930', '1774482936048641',
    '1775548501843970'
]

for did in cluster2_ids:
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
