#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

cluster5_ids = [
    '1843309449749698', '1843309500205058', '1853377390815233', '1853377803841537',
    '1875231879602658', '1875231912916994', '1875231953230418', '1879220213492353',
    '1868120855134226', '1868121865281538', '1853377811982657', '1863331595515009'
]

cluster6_ids = [
    '1843309514567809', '1847302878676994', '1847302895272962', '1847302908327938',
    '1847302920924306', '1847302935967746'
]

def check_cluster(name, doc_ids):
    print(f"================ {name} ================")
    for did in doc_ids:
        pattern = rf'(<a id="doc-{did}"></a>[\s\S]*?)(?=<a id="doc-\d+"></a>|$)'
        m = re.search(pattern, text)
        if m:
            sec = m.group(1)
            parts = sec.split('```')
            prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])
            print(f"=== DOC {did} ===")
            count = 0
            for line in prose.splitlines():
                line_str = line.strip()
                if not line_str:
                    continue
                if re.search(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note)\b', line_str, re.IGNORECASE):
                    print("  ", line_str[:120])
                    count += 1
                    if count >= 15:
                        print("   ... (more lines)")
                        break

check_cluster("CLUSTER 5", cluster5_ids)
check_cluster("CLUSTER 6", cluster6_ids)
