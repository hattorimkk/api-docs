from collections import Counter
import re

lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
lists = [l for l in lines if re.match(r"^(\-|\*|\d+\.)", l)]
counts = Counter(lists)
print(f"Total list items with English: {len(lists)}, Unique: {len(counts)}")
for l, c in counts.most_common(40):
    print(f"{c:3d}: {l[:100]}")
