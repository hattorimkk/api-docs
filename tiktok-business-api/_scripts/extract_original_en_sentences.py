#!/usr/bin/env python3
import os, sys, re
from collections import Counter

ROOT = "tiktok-business-api"
path = os.path.join(ROOT, "docs/08-use-cases/use-case-tao-chien-dich-p1.md")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
prose = "\n".join(prose_parts)

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
param_re = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')

en_paragraphs = []
for p in prose.split("\n\n"):
    ps = p.strip()
    if not ps or ps.startswith("<a id=") or ps.startswith("<!-- doc_id:"):
        continue
    # If it's pure parameter line, skip
    if param_re.match(ps):
        continue
    # Check if mostly English
    words = ps.split()
    if len(words) < 2:
        continue
    vi_words = sum(1 for w in words if vi_re.search(w))
    if vi_words / len(words) < 0.4:
        en_paragraphs.append(ps)

counts = Counter(en_paragraphs)
print(f"Total English paragraphs/blocks in ORIGINAL: {len(en_paragraphs)} (unique: {len(counts)})")

with open(os.path.join(ROOT, "_work/original_en_blocks.txt"), "w", encoding="utf-8") as f:
    for block, cnt in counts.most_common():
        f.write(f"{cnt:4d}\t{block.replace(chr(10), ' ⏎ ')}\n")

print("Top 30 frequent blocks:")
for block, cnt in counts.most_common(30):
    print(f"{cnt:3d}: {block.replace(chr(10), ' ')[:100]}")
