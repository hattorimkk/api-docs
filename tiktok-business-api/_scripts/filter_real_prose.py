#!/usr/bin/env python3
import os, sys, re

ROOT = "tiktok-business-api"
with open(os.path.join(ROOT, "_work/truly_untranslated.txt"), "r", encoding="utf-8") as f:
    entries = []
    for line in f:
        p = line.strip().split('\t', 1)
        if len(p) == 2:
            entries.append((int(p[0]), p[1]))

# Check if a line is just API field names or enum values or table dividers
def is_pure_technical(line):
    s = line.strip()
    # pure parameter list (words separated by space or bullet or or)
    tokens = re.split(r'[\s•|,]+', s)
    tokens = [t for t in tokens if t and t not in ('or', 'both', 'and', 'with', 'is', 'in', 'at', 'not', 'passed', 'to', 'for')]
    if not tokens:
        return True
    # If all tokens look like identifiers: snake_case, UPPER_CASE, CamelCase, or endpoint /.../
    all_ident = all(
        re.match(r'^[A-Za-z0-9_]+$', t) or t.startswith('/') or t.startswith('[') or t.startswith('`')
        for t in tokens
    )
    return all_ident

real_prose = [(c, l) for c, l in entries if not is_pure_technical(l)]
print(f"Total entries in truly_untranslated: {len(entries)}")
print(f"Real prose entries needing Vietnamese translation: {len(real_prose)}")
print("\nTop 40 Real Prose lines:")
for c, l in real_prose[:40]:
    print(f"{c:3d}: {l[:110]}")
