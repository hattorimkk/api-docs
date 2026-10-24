#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/residual_sentences.json') as f:
    items = json.load(f)

links = []
technical = []
real_prose = []

for it in items:
    l = it['line']
    if re.match(r'^[-*]\s*\[[^\]]+\]\([^)]+\)$', l):
        links.append(it)
    elif re.search(r'^[a-z0-9_`\s\-\.\,\(\)•\*/\\\[\]|]+$', l, re.IGNORECASE) and not re.search(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note)\b', l, re.IGNORECASE):
        technical.append(it)
    else:
        real_prose.append(it)

print(f"Total sentences: {len(items)}")
print(f"Pure markdown links: {len(links)}")
print(f"Technical parameter lines: {len(technical)}")
print(f"Real prose sentences: {len(real_prose)}")

with open('tiktok-business-api/_work/real_prose_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(real_prose, f, ensure_ascii=False, indent=2)

with open('tiktok-business-api/_work/residual_links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)

print("\n--- SAMPLE REAL PROSE SENTENCES (first 30) ---")
for it in real_prose[:30]:
    print(f"[{it['count']:2d}x] {repr(it['line'][:110])}")
