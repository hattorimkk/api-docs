#!/usr/bin/env python3
import os, sys, re
from collections import Counter

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/truly_untranslated.txt"), "r", encoding="utf-8") as f:
    lines = [line.strip().split('\t', 1)[1] for line in f if '\t' in line]

# Let's inspect short lines (<= 50 chars) which are typically Setting names or simple requirements
short_lines = [l for l in lines if len(l) <= 50 and not re.match(r'^[a-z_]+(\s+[a-z_]+)*$', l)]
print(f"Total short untranslated lines: {len(short_lines)}")
counts = Counter(short_lines)
print("Top 50 short lines:")
for l, c in counts.most_common(50):
    print(f"{c:3d}: {l}")
