import os
import re

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

lines = open(os.path.join(ROOT, "_work/remaining_step2.txt")).read().splitlines()

# Filter lines that have English phrases (not just (CTA), (Parameter), etc.)
def get_clean_en(text):
    # remove count
    p = text.split("\t", 1)
    line = p[1] if len(p) == 2 else p[0]
    
    # remove inline code
    s = re.sub(r"`[^`]+`", "", line)
    # remove urls
    s = re.sub(r"https?://\S+", "", s)
    # remove markdown links target
    s = re.sub(r"\]\([^\)]+\)", "]", s)
    
    # find words with >= 3 ascii letters
    words = re.findall(r"\b[A-Za-z]{3,}\b", s)
    allowed = {
        "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
        "api", "url", "id", "ids", "app", "web", "cta", "cbo", "ocpm", "cpc", "cpa", "roas"
    }
    filtered = [w for w in words if w.lower() not in allowed]
    return filtered, line

truly_untranslated = []
for l in lines:
    words, line = get_clean_en(l)
    if len(words) >= 2:
        cnt = int(l.split("\t")[0]) if "\t" in l else 1
        truly_untranslated.append((cnt, line))

print(f"Truly untranslated lines: {len(truly_untranslated)}")
with open(os.path.join(ROOT, "_work/truly_untranslated.txt"), "w", encoding="utf-8") as f:
    for c, l in truly_untranslated:
        f.write(f"{c:4d}\t{l}\n")

for c, l in truly_untranslated[:30]:
    print(f"{c:3d}: {l[:100]}")
