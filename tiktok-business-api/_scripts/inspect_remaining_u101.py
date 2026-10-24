#!/usr/bin/env python3
import os, sys, re
from collections import Counter

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)
sys.path.insert(0, _SCRIPT_DIR)

from u101_dict_structural import DOC_TITLES, BREADCRUMBS, HEADING_RULES
from u101_dict_tables import TABLE_PHRASE_RULES
from u101_dict_prose import PROSE_RULES
from u101_dict_creatives import CREATIVE_RULES
from u101_dict_bidding import BIDDING_RULES
from u101_dict_catalog import CATALOG_RULES
from u101_dict_targeting import TARGETING_RULES
from u101_dict_general import GENERAL_RULES
from u101_dict_major_blocks import MAJOR_BLOCK_RULES
from u101_dict_granular import GRANULAR_RULES
from u101_dict_blocks2 import BLOCKS2_RULES

path = os.path.join(ROOT, "docs/08-use-cases/use-case-tao-chien-dich-p1.md")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 0. Loại bỏ code mẫu python script rườm rà ở cuối file (Tuân thủ Quy tắc 4)
text = re.sub(r'### Python script mẫu\s*```python[\s\S]*?```', '', text)

# Tách header (chứa TOC) và các section
doc_marker_re = re.compile(r'(<a id="doc-(\d+)"></a>)')
matches = list(doc_marker_re.finditer(text))

sections = []
prev = 0
for i, m in enumerate(matches):
    start = m.start()
    sections.append((None if i == 0 else matches[i-1].group(2), text[prev:start]))
    prev = start
sections.append((matches[-1].group(2), text[prev:]))

all_rules = (
    BLOCKS2_RULES +
    GRANULAR_RULES +
    MAJOR_BLOCK_RULES +
    HEADING_RULES +
    TABLE_PHRASE_RULES +
    PROSE_RULES +
    CREATIVE_RULES +
    BIDDING_RULES +
    CATALOG_RULES +
    TARGETING_RULES +
    GENERAL_RULES
)

compiled_rules = [(re.compile(p, re.MULTILINE if ('^' in p or '$' in p) else 0), r) for p, r in all_rules]

processed_sections = []

# 1. Xử lý Header & TOC
header_did, header_text = sections[0]
def repl_toc(m):
    num = m.group(1)
    did = m.group(3)
    if did in DOC_TITLES:
        vi_title, en_title = DOC_TITLES[did]
        return f"- [{num}. {vi_title} ({en_title}) (#doc-{did})](#doc-{did})"
    return m.group(0)

header_text = re.sub(r'- \[(\d+)\.\s*([^\]]+?)\s*\(#doc-(\d+)\)\]\(#doc-\d+\)', repl_toc, header_text)
processed_sections.append(header_text)

# 2. Xử lý từng doc section
for did, sec_text in sections[1:]:
    parts = sec_text.split("```")
    new_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            new_parts.append(part)
        else:
            t = part
            if idx == 0:
                if did in DOC_TITLES:
                    vi_title, en_title = DOC_TITLES[did]
                    t = re.sub(r'^(<a id="doc-\d+"></a>\s*(?:<!--\s*doc_id:\s*\d+\s*-->\s*)+)#\s*[^\n]+',
                               rf'\1# {vi_title} (`{en_title}`)', t, flags=re.MULTILINE)
                if did in BREADCRUMBS:
                    t = re.sub(r'^> Đường dẫn:[^\n]+', BREADCRUMBS[did], t, flags=re.MULTILINE)

            for cregex, repl in compiled_rules:
                t = cregex.sub(repl, t)

            new_parts.append(t)

    processed_sections.append("```".join(new_parts))

new_text = "".join(processed_sections)

# Extract prose
parts = new_text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
prose = "\n".join(prose_parts)

lines = []
for l in prose.splitlines():
    ls = l.strip()
    if not ls or ls.startswith("<a id=") or ls.startswith("<!-- doc_id:"):
        continue
    # find words
    words = re.findall(r"\b[A-Za-z]{3,}\b", ls)
    allowed = {
        "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
        "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
        "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
    }
    filtered = [w for w in words if w.lower() not in allowed]
    if len(filtered) >= 3:
        lines.append(ls)

counts = Counter(lines)
print(f"Total prose lines remaining with >=3 English words: {len(lines)}")
print(f"Unique lines: {len(counts)}")
print("Top 30 frequent lines:")
for line, cnt in counts.most_common(30):
    print(f"{cnt:3d}: {line[:100]}")
