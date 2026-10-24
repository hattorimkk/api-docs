#!/usr/bin/env python3
import re
from collections import Counter

with open('tiktok-business-api/_work/outside_table_mixed.txt') as f:
    lines = [re.sub(r'^\[\d+ en words\]\s*', '', l).strip() for l in f]

# Find frequent subphrases of 3-6 words
words_in_lines = [l.split() for l in lines]
phrases = Counter()

for wl in words_in_lines:
    for i in range(len(wl) - 3):
        phrase = ' '.join(wl[i:i+4])
        # only if it looks mostly English
        if re.search(r'^[A-Za-z0-9_`\s\-\.\,\(\)•\*/\\\[\]\:\"]+$', phrase):
            phrases[phrase] += 1

print("--- TOP 40 ENGLISH SUBPHRASES OUTSIDE TABLES ---")
for p, cnt in phrases.most_common(40):
    print(f"[{cnt:2d}x] {repr(p)}")
