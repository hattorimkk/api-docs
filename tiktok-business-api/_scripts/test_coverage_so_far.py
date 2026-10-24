#!/usr/bin/env python3
import json, re, sys
sys.path.insert(0, 'tiktok-business-api/_scripts')

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

all_rule_lists = [
    ("heading_rules", d_struct.HEADING_RULES),
    ("tables", d_tables.TABLE_PHRASE_RULES),
    ("prose", d_prose.PROSE_RULES),
    ("creatives", d_creatives.CREATIVE_RULES),
    ("bidding", d_bidding.BIDDING_RULES),
    ("catalog", d_catalog.CATALOG_RULES),
    ("targeting", d_targeting.TARGETING_RULES),
    ("general", d_general.GENERAL_RULES),
    ("major", d_major.MAJOR_BLOCK_RULES),
    ("granular", d_granular.GRANULAR_RULES),
    ("blocks2", d_blocks2.BLOCKS2_RULES),
    ("batch1", d_b1.BATCH1_RULES),
    ("batch2", d_b2.BATCH2_RULES),
    ("batch3", d_b3.BATCH3_RULES),
    ("batch4", d_b4.BATCH4_RULES),
    ("batch5", d_b5.BATCH5_RULES),
    ("common_clauses", d_cc.COMMON_CLAUSE_RULES),
    ("cluster1", d_c1.CLUSTER1_RULES),
    ("cluster2", d_c2.CLUSTER2_RULES),
    ("cluster3", d_c3.CLUSTER3_RULES),
]

compiled_rules = []
for name, rules in all_rule_lists:
    for item in rules:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            pattern, repl = item[0], item[1]
            try:
                compiled_rules.append((re.compile(pattern), repl))
            except Exception as e:
                print(f"Error compiling pattern in {name}: {pattern[:50]}... -> {e}")

print(f"Total compiled regex rules so far: {len(compiled_rules)}")

with open('tiktok-business-api/_work/all_1501_en_lines.json') as f:
    items = json.load(f)

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
param_re = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')

untouched = []
modified = []

for item in items:
    line = item['line']
    cnt = item['count']
    
    cur = line
    for reg, repl in compiled_rules:
        cur = reg.sub(repl, cur)
        
    if vi_re.search(cur) or cur != line:
        modified.append({"orig": line, "cur": cur, "count": cnt})
    else:
        untouched.append({"orig": line, "cur": cur, "count": cnt})

print(f"Out of 1501 unique English lines:")
print(f"  Translated or partially modified: {len(modified)}")
print(f"  Untouched: {len(untouched)}")

with open('tiktok-business-api/_work/untouched_after_c3.json', 'w', encoding='utf-8') as f:
    json.dump(untouched, f, ensure_ascii=False, indent=2)

print("Saved untouched lines to tiktok-business-api/_work/untouched_after_c3.json")
