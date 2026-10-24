#!/usr/bin/env python3
import os, sys, re
from collections import Counter

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/truly_untranslated.txt"), "r", encoding="utf-8") as f:
    lines = [line.strip().split('\t', 1)[1] for line in f if '\t' in line]

med_lines = [l for l in lines if 50 < len(l) <= 150 and not re.match(r'^[a-z_]+(\s+[a-z_]+)*$', l)]
long_lines = [l for l in lines if len(l) > 150 and not re.match(r'^[a-z_]+(\s+[a-z_]+)*$', l)]

print(f"Total medium untranslated lines (51-150 chars): {len(med_lines)}")
print(f"Total long untranslated lines (>150 chars): {len(long_lines)}")

print("\n--- Sample 20 Medium Lines ---")
for l in med_lines[:20]:
    print("MED:", l)

print("\n--- Sample 20 Long Lines ---")
for l in long_lines[:20]:
    print("LONG:", l)
