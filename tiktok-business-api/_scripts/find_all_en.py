import re
import os

path = "tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

# Collect lines that have English
en_lines = []
for p in prose_parts:
    for line in p.splitlines():
        line_s = line.strip()
        if not line_s:
            continue
        # Skip doc markers
        if line_s.startswith("<a id=") or line_s.startswith("<!-- doc_id:"):
            continue
        # Check if line contains common english words
        # Count ascii alpha words
        words = re.findall(r"\b[A-Za-z]{3,}\b", line_s)
        # Filter out common technical keywords that stay in English like curl, api, id, json, etc.
        tech_words = {"curl", "api", "id", "url", "json", "http", "https", "post", "get", "app", "web", "tiktok", "lead", "traffic", "doc"}
        filtered = [w for w in words if w.lower() not in tech_words]
        if len(filtered) >= 3:
            en_lines.append(line_s)

print(f"Total lines with English: {len(en_lines)}")
with open("tiktok-business-api/_work/u101_en_lines.txt", "w", encoding="utf-8") as out:
    for l in en_lines:
        out.write(l + "\n")
print("Written to _work/u101_en_lines.txt")
