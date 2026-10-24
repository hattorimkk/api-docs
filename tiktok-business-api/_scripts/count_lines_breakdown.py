#!/usr/bin/env python3
with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split('```')
code_lines = sum(len(p.splitlines()) for i, p in enumerate(parts) if i % 2 == 1)
prose_lines = sum(len(p.splitlines()) for i, p in enumerate(parts) if i % 2 == 0)

print(f"Total lines: {len(text.splitlines())}")
print(f"Code block lines: {code_lines}")
print(f"Prose lines: {prose_lines}")
