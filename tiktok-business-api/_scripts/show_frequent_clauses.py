#!/usr/bin/env python3
with open('tiktok-business-api/_work/frequent_clauses.txt') as f:
    entries = [line.strip().split('\t', 1) for line in f if '\t' in line]

for cnt, text in entries[:100]:
    print(f"{int(cnt):2d}: {text}")
