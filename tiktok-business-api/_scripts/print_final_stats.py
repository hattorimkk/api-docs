#!/usr/bin/env python3
with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
code_blocks = text.count('```') // 2

print(f"Total lines: {len(lines):,}")
print(f"Total words: {len(words):,}")
print(f"Total code blocks: {code_blocks:,}")
print(f"Total bytes: {len(text.encode('utf-8')):,}")
