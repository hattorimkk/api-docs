import os
import re

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

lines = open(os.path.join(ROOT, "_work/remaining_step2.txt")).read().splitlines()

vn_chars = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
               "ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ")

pure_en_lines = []
partially_en_lines = []

for l in lines:
    parts = l.split("\t", 1)
    cnt = int(parts[0]) if len(parts) == 2 else 1
    text = parts[1] if len(parts) == 2 else l
    
    # Check proportion of Vietnamese accented words
    words = text.split()
    vn_word_count = sum(1 for w in words if any(c in vn_chars for c in w))
    
    if vn_word_count == 0:
        pure_en_lines.append((cnt, text))
    elif vn_word_count < len(words) * 0.4:
        # mostly English with a few Vietnamese words
        partially_en_lines.append((cnt, text))

print(f"Pure English lines: {len(pure_en_lines)} (total occ: {sum(c for c, t in pure_en_lines)})")
print(f"Mostly English lines: {len(partially_en_lines)} (total occ: {sum(c for c, t in partially_en_lines)})")

with open(os.path.join(ROOT, "_work/to_translate_final.txt"), "w", encoding="utf-8") as f:
    f.write("=== PURE ENGLISH LINES ===\n")
    for c, t in pure_en_lines:
        f.write(f"{c:4d}\t{t}\n")
    f.write("\n=== MOSTLY ENGLISH LINES ===\n")
    for c, t in partially_en_lines:
        f.write(f"{c:4d}\t{t}\n")
