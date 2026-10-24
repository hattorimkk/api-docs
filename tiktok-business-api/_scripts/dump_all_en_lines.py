#!/usr/bin/env python3
import json, re
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

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
param_re = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')

en_prose_lines = [l for l in content_lines if not vi_re.search(l) and not param_re.match(l)]
counts = Counter(en_prose_lines)

data = [{"line": l, "count": c} for l, c in counts.most_common()]
with open('tiktok-business-api/_work/all_1501_en_lines.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(data)} lines to _work/all_1501_en_lines.json")
