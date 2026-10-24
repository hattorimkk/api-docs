#!/usr/bin/env python3
import re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)

outside_table_mixed = []
table_mixed = []

for p in prose_parts:
    for line in p.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith('<a id=') or line_str.startswith('<!-- doc_id:'):
            continue
        matches = en_word_re.findall(line_str)
        if len(matches) >= 2: # 2 or more English words
            if line_str.startswith('|'):
                table_mixed.append((line_str, len(matches)))
            else:
                outside_table_mixed.append((line_str, len(matches)))

print(f"Total prose lines outside tables with English: {len(outside_table_mixed)}")
print(f"Total table lines with English: {len(table_mixed)}")

with open('tiktok-business-api/_work/outside_table_mixed.txt', 'w', encoding='utf-8') as f:
    for l, cnt in outside_table_mixed:
        f.write(f"[{cnt} en words] {l}\n")

print("\n--- FIRST 25 OUTSIDE TABLE MIXED ---")
for l, cnt in outside_table_mixed[:25]:
    print(f"[{cnt}x] {l[:110]}")
