#!/usr/bin/env python3
with open('tiktok-business-api/_work/frequent_clauses.txt') as f:
    entries = [line.strip().split('\t', 1) for line in f if '\t' in line]

ge_2 = [e for e in entries if int(e[0]) >= 2]
print(f"Total clauses with count >= 2: {len(ge_2)} (sum: {sum(int(e[0]) for e in ge_2)})")
