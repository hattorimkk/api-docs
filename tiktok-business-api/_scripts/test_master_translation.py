#!/usr/bin/env python3
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import u101_dict_structural as d_struct
import u101_dict_tables as d_tables
import u101_dict_prose as d_prose
import u101_dict_creatives as d_creatives
import u101_dict_bidding as d_bidding
import u101_dict_catalog as d_catalog
import u101_dict_targeting as d_targeting
import u101_dict_general as d_general
import u101_dict_major_blocks as d_major
import u101_dict_granular as d_granular
import u101_dict_blocks2 as d_blocks2

import u101_dict_batch1 as d_b1
import u101_dict_batch2 as d_b2
import u101_dict_batch3 as d_b3
import u101_dict_batch4 as d_b4
import u101_dict_batch5 as d_b5

import u101_trans_common_clauses as d_cc
import u101_trans_cluster1 as d_c1
import u101_trans_cluster2 as d_c2
import u101_trans_cluster3 as d_c3
import u101_trans_cluster4 as d_c4
import u101_trans_cluster5 as d_c5
import u101_trans_cluster6 as d_c6
import u101_trans_common_residual as d_res
import u101_trans_residual_part1 as d_rp1
import u101_trans_residual_part2 as d_rp2
import u101_trans_residual_part3 as d_rp3
import u101_final_closure as d_closure
import u101_exact_186 as d_exact

rule_groups = [
    ("major", d_major.MAJOR_BLOCK_RULES),
    ("blocks2", d_blocks2.BLOCKS2_RULES),
    ("cluster1", d_c1.CLUSTER1_RULES),
    ("cluster2", d_c2.CLUSTER2_RULES),
    ("cluster3", d_c3.CLUSTER3_RULES),
    ("cluster4", d_c4.CLUSTER4_RULES),
    ("cluster5", d_c5.CLUSTER5_RULES),
    ("cluster6", d_c6.CLUSTER6_RULES),
    ("final_closure", d_closure.FINAL_CLOSURE_RULES),
    ("residual_part1", d_rp1.RESIDUAL_PART1_RULES),
    ("residual_part2", d_rp2.RESIDUAL_PART2_RULES),
    ("residual_part3", d_rp3.RESIDUAL_PART3_RULES),
    ("batch1", d_b1.BATCH1_RULES),
    ("batch2", d_b2.BATCH2_RULES),
    ("batch3", d_b3.BATCH3_RULES),
    ("batch4", d_b4.BATCH4_RULES),
    ("batch5", d_b5.BATCH5_RULES),
    ("common_clauses", d_cc.COMMON_CLAUSE_RULES),
    ("common_residual", d_res.COMMON_RESIDUAL_RULES),
    ("prose", d_prose.PROSE_RULES),
    ("bidding", d_bidding.BIDDING_RULES),
    ("catalog", d_catalog.CATALOG_RULES),
    ("targeting", d_targeting.TARGETING_RULES),
    ("creatives", d_creatives.CREATIVE_RULES),
    ("tables", d_tables.TABLE_PHRASE_RULES),
    ("heading_rules", d_struct.HEADING_RULES),
    ("general", d_general.GENERAL_RULES),
    ("granular", d_granular.GRANULAR_RULES),
]

compiled_rules = []
for name, rules in rule_groups:
    for item in rules:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            pattern, repl = item[0], item[1]
            try:
                compiled_rules.append((re.compile(pattern, re.MULTILINE), repl))
            except Exception as e:
                print(f"Error compiling in {name}: {e}")

print(f"Total compiled rules: {len(compiled_rules)}")
print(f"Total exact 186 rules: {len(d_exact.EXACT_186_MAP)}")

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md', 'r', encoding='utf-8') as f:
    orig_text = f.read()

# Remove redundant trailing python script if present
split_point = orig_text.find("### Python script mẫu")
if split_point != -1:
    print(f"Found trailing Python script at {split_point}, removing it...")
    text_to_process = orig_text[:split_point].rstrip() + "\n"
else:
    text_to_process = orig_text

# Apply doc titles and breadcrumbs doc by doc
docs = re.split(r'(?=<a id="doc-\d+"></a>)', text_to_process)
processed_docs = []

for d in docs:
    m = re.search(r'<a id="doc-(\d+)"></a>', d)
    if not m:
        processed_docs.append(d)
        continue
    did = m.group(1)
    cur_doc = d
    
    # Breadcrumbs replacement
    if did in d_struct.BREADCRUMBS:
        new_bc = d_struct.BREADCRUMBS[did]
        cur_doc = re.sub(r'>\s*Đường dẫn:\s*Use Cases[^\n]+', new_bc, cur_doc)
        cur_doc = re.sub(r'>\s*Path:\s*Use Cases[^\n]+', new_bc, cur_doc)
        
    # Doc titles replacement
    if did in d_struct.DOC_TITLES:
        vi_t, en_t = d_struct.DOC_TITLES[did]
        cur_doc = re.sub(r'#\s+`?' + re.escape(en_t) + r'`?', f'# {vi_t} (`{en_t}`)', cur_doc)
        cur_doc = re.sub(r'#\s+' + re.escape(vi_t) + r'\s+\(`?' + re.escape(en_t) + r'`?\)', f'# {vi_t} (`{en_t}`)', cur_doc)
        
    processed_docs.append(cur_doc)

combined_text = "".join(processed_docs)

# Now preserve code blocks and translate prose
parts = combined_text.split("```")
print(f"Total blocks (prose + code): {len(parts)}")

new_parts = []
for i, part in enumerate(parts):
    if i % 2 == 1:
        # Code block -> KEEP EXACTLY AS IS
        new_parts.append(part)
    else:
        # Prose block
        cur = part
        for reg, repl in compiled_rules:
            cur = reg.sub(repl, cur)
            
        for orig, repl in d_exact.EXACT_186_MAP.items():
            cur = cur.replace(orig, repl)
            
        new_parts.append(cur)

result_text = "```".join(new_parts)

# Write to test file
with open('tiktok-business-api/_work/u101_dry_run.md', 'w', encoding='utf-8') as f:
    f.write(result_text)

print(f"Dry run saved to tiktok-business-api/_work/u101_dry_run.md")

# Analyze remaining English in prose
parts_res = result_text.split("```")
prose_res = [parts_res[i] for i in range(0, len(parts_res), 2)]
all_lines = []
for p in prose_res:
    all_lines.extend(p.splitlines())

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]|\b(trang|web|quang|cao|chien|dich|nhom|cai|dat|yeu|cau|tham|so|danh|muc|muc|tieu|gia|thau|dong|mo|ta|nguoi|dung|khach|hang|ung|dung|tien|ich|san|pham)\b', re.IGNORECASE)
param_re = re.compile(r'^[a-z0-9_`\s\-\.\,\(\)•\*/\\\[\]|]+$', re.IGNORECASE)

non_empty = [l.strip() for l in all_lines if l.strip()]
content_lines = [l for l in non_empty if not (l.startswith('<a id=') or l.startswith('<!-- doc_id:'))]

remaining_en = [l for l in content_lines if not vi_re.search(l) and not param_re.match(l)]

tech_markers = {
    'N/A', '✅', '❌', '> [!NOTE]', '> **Important:**', '> [!IMPORTANT]', '> **Note**:',
    '|---|---|---|', '|---|---|---|---|', '|---|---|', '|---|---|---|---|---|',
    'PLACEMENT_TYPE_NORMAL', 'APP_PROMOTION', 'WEBSITE', 'CATALOG', '["PLACEMENT_TIKTOK"]',
    'LEAD_GENERATION', 'WEB_CONVERSIONS', 'SINGLE_VIDEO', 'APP_INSTALL', 'TRAFFIC', 'ENGAGEMENT',
    'TIKTOK', 'TIKTOK_SHOP', 'PRODUCT_SALES', 'OFFLINE', 'STORE', 'LIVE_SHOPPING',
    'TikTok', 'TikTok Shop', 'Pixel', 'oCPM', '18+', 'App', '* TikTok Business Center',
    '| `ID` | Indonesia |', '| `MY` | Malaysia |', '| `PH` | Philippines |', '| `SG` | Singapore |',
    '| `TH` | Thái Lan |', '| `VN` | Việt Nam |', '| `US` | Hoa Kỳ |',
    '- [API GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000911166465)'
}
true_remaining = [l for l in remaining_en if l not in tech_markers and not re.match(r'^[A-Z0-9_\[\]",\s\.\-]+$', l)]
from collections import Counter
c_true = Counter(true_remaining)

print(f"\nTotal non-empty prose lines in dry run: {len(content_lines)}")
print(f"Lines without Vietnamese: {len(remaining_en)}")
print(f"True remaining prose lines: {len(true_remaining)} (unique: {len(c_true)})")

if true_remaining:
    print("\nRemaining lines:")
    for l, cnt in c_true.most_common(20):
        print(f"[{cnt:2d}x] {repr(l[:100])}")
else:
    print("\nPERFECT! 0 TRUE REMAINING PROSE LINES!")
