#!/usr/bin/env python3
with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split('```')
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
all_prose_lines = []
for p in prose_parts:
    all_prose_lines.extend(p.splitlines())

non_empty = [l.strip() for l in all_prose_lines if l.strip()]
tag_lines = [l for l in non_empty if l.startswith('<a id=') or l.startswith('<!-- doc_id:')]
content_lines = [l for l in non_empty if not (l.startswith('<a id=') or l.startswith('<!-- doc_id:'))]

print(f"Total prose lines: {len(all_prose_lines)}")
print(f"Non-empty prose lines: {len(non_empty)}")
print(f"Doc tag lines: {len(tag_lines)}")
print(f"Actual content lines: {len(content_lines)}")
