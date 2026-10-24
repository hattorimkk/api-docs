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

# Filter out lines that are just parameter names (lowercase with underscores)
param_pattern = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')
real_sentences = []
for cnt, txt in entries:
    if param_pattern.match(txt.strip()):
        continue
    # must have uppercase or punctuation typical of sentences
    real_sentences.append((cnt, txt))

print(f"Total real untranslated sentences/paragraphs: {len(real_sentences)} unique (sum occurrences: {sum(c for c, _ in real_sentences)})")
print("\nTop 40 Real Untranslated Sentences:")
for cnt, txt in real_sentences[:40]:
    print(f"{cnt:3d}: {txt[:110]}")
