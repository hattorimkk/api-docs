with open("/tmp/pure_en_prose.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_lines = []
for l in lines:
    parts = l.split(": ", 1)
    if len(parts) == 2:
        clean_lines.append(parts[1].strip())

unique_lines = list(set(clean_lines))
print(f"Total lines: {len(clean_lines)}, Unique lines: {len(unique_lines)}")

with open("/tmp/unique_pure_en_prose.txt", "w", encoding="utf-8") as out:
    for u in sorted(unique_lines):
        out.write(u + "\n")
