from collections import Counter
import re

lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
others = [l for l in lines if not (l.startswith("#") or l.startswith(">") or l.startswith("|") or re.match(r"^(\-|\*|\d+\.)", l))]

counts = Counter(others)
print(f"Total other lines: {len(others)}, Unique: {len(counts)}")
for o, c in counts.most_common(40):
    print(f"{c:3d}: {o[:100]}")
