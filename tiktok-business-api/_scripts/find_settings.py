import re
from collections import Counter

txt = open("tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md").read()

# Setting names usually appear in tables after "Setting" or in pipe tables
# In 4-line tables:
# Setting \n Requirement \n Parameter \n How to configure
blocks = re.findall(r"(?:Thiết lập \(Setting\)|Setting)\n(?:Yêu cầu \(Requirement\)|Requirement)\n(?:Tham số \(Parameter\)|Parameter)\n(?:Hướng dẫn cấu hình tham số|How to configure[^\n]*)\n\n([\s\S]*?)(?=\n###|\n##|\n---|\Z)", txt)

settings = []
for b in blocks:
    # each item has 4 parts
    chunks = [c.strip() for c in b.split("\n\n") if c.strip()]
    for c in chunks:
        lines = c.splitlines()
        if len(lines) >= 1:
            settings.append(lines[0])

counts = Counter(settings)
print(f"Total setting items in 4-line tables: {len(settings)}, unique: {len(counts)}")
for s, cnt in counts.most_common(50):
    print(f"{cnt:3d}: {s[:80]}")
