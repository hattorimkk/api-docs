import re
import os

path = "tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md"
with open(path, "r", encoding="utf-8") as f:
    txt = f.read()

parts = txt.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

samples = []
for p in prose_parts:
    for s in p.splitlines():
        s = s.strip()
        if not s or s.startswith("#") or s.startswith("|") or s.startswith("<") or s.startswith("- ["):
            continue
        words = s.split()
        if len(words) >= 4:
            ascii_words = [w for w in words if re.match(r"^[A-Za-z]+$", w)]
            if len(ascii_words) / len(words) > 0.5:
                samples.append(s)

print(f"Found {len(samples)} lines with predominantly English prose.")
for s in samples[:50]:
    print("---", s[:120])
