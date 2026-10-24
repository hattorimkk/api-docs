#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

cluster4_ids = [
    '1758528372513794', '1822009058467842', '1822009220448257', '1822009242546258',
    '1768006268820546', '1827645480080385', '1814122471133186', '1814122492598274'
]

for did in cluster4_ids:
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
            # if contains common English words
            if re.search(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note)\b', line_str, re.IGNORECASE):
                print("  ", line_str[:120])
                count += 1
                if count >= 20:
                    print("   ... (more lines)")
                    break
