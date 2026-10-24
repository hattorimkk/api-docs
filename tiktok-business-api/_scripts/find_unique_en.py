import re
from collections import Counter

path = "tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

lines = []
for p in prose_parts:
    for l in p.splitlines():
        ls = l.strip()
        if ls:
            lines.append(ls)

# Check English lines
en_lines = []
for l in lines:
    if l.startswith("<a id=") or l.startswith("<!-- doc_id:"):
        continue
    words = re.findall(r"\b[A-Za-z]{3,}\b", l)
    tech_words = {"curl", "api", "id", "url", "json", "http", "https", "post", "get", "app", "web", "tiktok", "lead", "traffic", "doc"}
    filtered = [w for w in words if w.lower() not in tech_words]
    if len(filtered) >= 2:
        en_lines.append(l)

counts = Counter(en_lines)
print(f"Total unique English lines: {len(counts)}")
with open("tiktok-business-api/_work/u101_unique_en_lines.txt", "w", encoding="utf-8") as f:
    for l, c in counts.most_common():
        f.write(f"{c:4d}\t{l}\n")
print("Written to _work/u101_unique_en_lines.txt")
