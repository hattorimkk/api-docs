from collections import Counter
import re

lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
headings = [l for l in lines if l.startswith("#")]
counts = Counter(headings)
print(f"Unique headings: {len(counts)}")
for h, c in counts.most_common(40):
    print(f"{c:3d}: {h}")
