#!/usr/bin/env python3
import os

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/original_en_blocks.txt"), "r", encoding="utf-8") as f:
    blocks = [line.strip().split('\t', 1)[1] for line in f if '\t' in line]

total_chars = sum(len(b) for b in blocks)
print(f"Total unique blocks: {len(blocks)}, total characters: {total_chars}")
