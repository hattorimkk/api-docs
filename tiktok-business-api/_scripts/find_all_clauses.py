#!/usr/bin/env python3
import os, sys, re
from collections import Counter

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/truly_untranslated.txt"), "r", encoding="utf-8") as f:
    entries = []
    for line in f:
        p = line.strip().split('\t', 1)
        if len(p) == 2:
            entries.append((int(p[0]), p[1]))

# Split into individual sentences / clauses
clauses = []
for cnt, line in entries:
    # split by bullets, periods followed by space, or newlines
    parts = re.split(r'(?:•|\n|\. (?=[A-Z]))', line)
    for p in parts:
        ps = p.strip().rstrip('.')
        if len(ps) >= 15:
            # check if mostly English
            words = ps.split()
            vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
            vi_words = sum(1 for w in words if vi_re.search(w))
            if vi_words / max(1, len(words)) < 0.4:
                # filter pure technical
                if not re.match(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$', ps):
                    clauses.append(ps)

counts = Counter(clauses)
print(f"Total extracted clauses: {len(clauses)}, unique clauses: {len(counts)}")
print("\nTop 50 Most Frequent Clauses:")
for c, cnt in counts.most_common(50):
    print(f"{cnt:3d}: {c[:100]}")

with open(os.path.join(ROOT, "_work/frequent_clauses.txt"), "w", encoding="utf-8") as f:
    for c, cnt in counts.most_common():
        f.write(f"{cnt:4d}\t{c}\n")
