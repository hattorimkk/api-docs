#!/usr/bin/env python3
import os, sys, re
from collections import Counter

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/remaining_round1.txt"), "r", encoding="utf-8") as f:
    entries = []
    for line in f:
        p = line.strip().split('\t', 1)
        if len(p) == 2:
            entries.append((int(p[0]), p[1]))

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
pure_en = [e for e in entries if not vi_re.search(e[1])]
mostly_en = []
for cnt, txt in entries:
    words = txt.split()
    if len(words) >= 4:
        vi_words = [w for w in words if vi_re.search(w)]
        if len(vi_words) / len(words) < 0.4:
            mostly_en.append((cnt, txt))

print(f"Total entries: {len(entries)}")
print(f"Pure EN (no Vietnamese): {len(pure_en)} unique, {sum(c for c, _ in pure_en)} total occurrences")
print(f"Mostly EN (<40% Vietnamese): {len(mostly_en)} unique, {sum(c for c, _ in mostly_en)} total occurrences")

print("\n--- Top 30 Pure EN ---")
for cnt, txt in pure_en[:30]:
    print(f"{cnt:3d}: {txt[:100]}")

print("\n--- Top 30 Mostly EN ---")
for cnt, txt in mostly_en[:30]:
    print(f"{cnt:3d}: {txt[:100]}")
