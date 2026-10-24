#!/usr/bin/env python3
import re
from collections import Counter

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split('```')
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
all_prose_lines = []
for p in prose_parts:
    all_prose_lines.extend(p.splitlines())

non_empty = [l.strip() for l in all_prose_lines if l.strip()]
content_lines = [l for l in non_empty if not (l.startswith('<a id=') or l.startswith('<!-- doc_id:'))]

print(f"Total content lines: {len(content_lines)}")
print(f"Unique content lines: {len(set(content_lines))}")

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
param_re = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')

vi_lines = [l for l in content_lines if vi_re.search(l)]
en_param_lines = [l for l in content_lines if not vi_re.search(l) and param_re.match(l)]
en_prose_lines = [l for l in content_lines if not vi_re.search(l) and not param_re.match(l)]

print(f"Lines already containing Vietnamese: {len(vi_lines)} (unique: {len(set(vi_lines))})")
print(f"Pure English parameter name lines: {len(en_param_lines)} (unique: {len(set(en_param_lines))})")
print(f"English prose lines needing translation: {len(en_prose_lines)} (unique: {len(set(en_prose_lines))})")
