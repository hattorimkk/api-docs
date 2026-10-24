import re
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

lines = open(os.path.join(ROOT, "_work/remaining_en.txt")).read().splitlines()
vn_chars = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
               "ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ")

mixed_with_en_phrase = []
for l in lines:
    parts = l.split("\t", 1)
    cnt = int(parts[0]) if len(parts) == 2 else 1
    text = parts[1] if len(parts) == 2 else l
    if any(c in vn_chars for c in text):
        # find sequences of 3+ english words
        m = re.findall(r"\b[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\b", text)
        if m:
            mixed_with_en_phrase.append((cnt, text, m))

print(f"Mixed lines with 3+ consecutive English words: {len(mixed_with_en_phrase)}")
with open(os.path.join(ROOT, "_work/mixed_with_en_phrase.txt"), "w", encoding="utf-8") as f:
    for c, t, m in mixed_with_en_phrase:
        f.write(f"{c:4d}\t{t}\n\t--> Phrases: {m}\n")

for c, t, m in mixed_with_en_phrase[:30]:
    print(f"{c:3d}: {t[:90]} | {m}")
