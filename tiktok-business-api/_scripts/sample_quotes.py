from collections import Counter

lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
quotes = [l for l in lines if l.startswith(">")]
counts = Counter(quotes)
print(f"Unique quotes: {len(counts)}")
for q, c in counts.most_common(30):
    print(f"{c:3d}: {q[:120]}")
