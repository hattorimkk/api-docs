import re
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

lines = open(os.path.join(ROOT, "_work/remaining_en.txt")).read().splitlines()

vn_chars = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
               "ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ")

pure_en = []
for l in lines:
    parts = l.split("\t", 1)
    if len(parts) == 2:
        cnt = int(parts[0])
        text = parts[1]
    else:
        cnt = 1
        text = l
    
    # check if text has any Vietnamese accented characters
    if not any(c in vn_chars for c in text):
        pure_en.append((cnt, text))

print(f"Lines with ZERO Vietnamese characters: {len(pure_en)}")
with open(os.path.join(ROOT, "_work/pure_en.txt"), "w", encoding="utf-8") as f:
    for c, t in pure_en:
        f.write(f"{c:4d}\t{t}\n")

print("Top 50 pure English lines:")
for c, t in pure_en[:50]:
    print(f"{c:3d}: {t[:100]}")
