#!/usr/bin/env python3
import os, sys, re
ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/original_en_blocks.txt"), "r", encoding="utf-8") as f:
    blocks = [line.strip().split('\t', 1) for line in f if '\t' in line]

multiline = []
for cnt_s, block in blocks:
    b = block.replace(' ⏎ ', '\n').strip()
    if '\n' in b and not b.startswith('#') and not b.startswith('>') and not b.startswith('|'):
        multiline.append((int(cnt_s), b))

print(f"Total multiline blocks: {len(multiline)}")
for i, (cnt, b) in enumerate(multiline[:20]):
    print(f"\n--- [{i+1}] (occurrences: {cnt}) ---")
    print(b[:250])
