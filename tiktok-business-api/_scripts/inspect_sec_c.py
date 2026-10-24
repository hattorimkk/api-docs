with open("/tmp/sec_c.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

print(f"Total lines in sec_c: {len(lines)}")
for i, l in enumerate(lines[:35]):
    print(f"{i+1}: {l[:90]}")
