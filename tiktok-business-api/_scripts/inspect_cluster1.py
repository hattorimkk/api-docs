#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

cluster1_ids = ['1758526151905281', '1782086026530817', '1782086241778690', '1808164002093058', '1772549012687873']

# Extract text of each doc
for did in cluster1_ids:
    pattern = rf'(<a id="doc-{did}"></a>[\s\S]*?)(?=<a id="doc-\d+"></a>|$)'
    m = re.search(pattern, text)
    if m:
        sec = m.group(1)
        # get prose
        parts = sec.split('```')
        prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])
        print(f"=== DOC {did} ===")
        for line in prose.splitlines()[:15]:
            if line.strip():
                print("  ", line[:100])
