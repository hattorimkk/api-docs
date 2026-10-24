import re
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

from test_engine import new_text

parts = new_text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]

paragraphs = []
for p in prose_parts:
    for para in p.split("\n\n"):
        para_s = para.strip()
        if not para_s or para_s.startswith("<a id=") or para_s.startswith("<!-- doc_id:"):
            continue
        words = para_s.split()
        if len(words) >= 10:
            ascii_words = [w for w in words if re.match(r"^[A-Za-z]+$", w)]
            if len(ascii_words) / len(words) > 0.6:
                paragraphs.append((len(words), para_s))

paragraphs.sort(key=lambda x: x[0], reverse=True)
print(f"Predominantly English paragraphs remaining: {len(paragraphs)}")
for idx, (count, para) in enumerate(paragraphs[:15]):
    print(f"\n--- Paragraph {idx+1} ({count} words) ---")
    print(para[:400])
