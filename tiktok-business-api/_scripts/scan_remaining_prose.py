import re

FILE_PATH = "tiktok-business-api/docs/09-marketing-api/do-luong-quang-cao-tom-tat.md"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_code = False
en_prose_lines = []

for idx, line in enumerate(lines):
    raw = line.strip()
    if raw.startswith("```"):
        in_code = not in_code
        continue
    if in_code:
        continue
    # Exclude table lines, anchors, comments, empty lines
    if not raw or raw.startswith("|") or raw.startswith("<!--") or raw.startswith("<a id=") or raw.startswith("---"):
        continue
    
    # Check if line contains English sentences or words (e.g. 3+ consecutive English words or common English verbs/prepositions)
    # Exclude pure links or tags like `[link](url)`
    clean_line = re.sub(r'\[.*?\]\(.*?\)', '', raw)
    clean_line = re.sub(r'`.*?`', '', clean_line)
    
    # If clean_line contains English words
    words = re.findall(r'\b[A-Za-z]{3,}\b', clean_line)
    if len(words) >= 3:
        en_prose_lines.append((idx + 1, raw))

print(f"Total English prose lines found: {len(en_prose_lines)}")
with open("/tmp/remaining_en_prose.txt", "w", encoding="utf-8") as out:
    for line_num, text in en_prose_lines:
        out.write(f"Line {line_num}: {text}\n")

for line_num, text in en_prose_lines[:25]:
    print(f"Line {line_num}: {text[:100]}")
