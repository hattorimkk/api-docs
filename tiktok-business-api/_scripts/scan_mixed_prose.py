#!/usr/bin/env python3
import re, json
from collections import Counter

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('```')
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)

outside_table_lines = []

for p in prose_parts:
    for line in p.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith('<a id=') or line_str.startswith('<!-- doc_id:'):
            continue
        if line_str.startswith('|'):
            continue
        matches = en_word_re.findall(line_str)
        if len(matches) >= 2:
            outside_table_lines.append(line_str)

print(f"Total prose lines outside tables with English (>=2 en words): {len(outside_table_lines)}")

# Save unique lines
c = Counter(outside_table_lines)
print(f"Unique lines: {len(c)}")
with open('tiktok-business-api/_work/current_outside_table_mixed.json', 'w', encoding='utf-8') as f:
    json.dump([{"line": l, "count": cnt} for l, cnt in c.most_common()], f, ensure_ascii=False, indent=2)
