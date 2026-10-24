lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
tables = [l for l in lines if l.startswith("|")]
print(f"Total pipe table rows with English: {len(tables)}")
for t in tables[:30]:
    print("---", t[:120])
