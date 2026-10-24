#!/usr/bin/env python3
import re
from collections import Counter

with open('tiktok-business-api/_work/u101_dry_run.md') as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
all_lines = []
for p in prose_parts:
    all_lines.extend(p.splitlines())

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]')
param_re = re.compile(r'^[a-z_`\s\-\.\,\(\)•\*/\\\[\]\d]+$')

non_empty = [l.strip() for l in all_lines if l.strip()]
content_lines = [l for l in non_empty if not (l.startswith('<a id=') or l.startswith('<!-- doc_id:'))]

remaining_en = [l for l in content_lines if not vi_re.search(l) and not param_re.match(l)]
c = Counter(remaining_en)

# Exclude technical markers
tech_markers = {
    'N/A', '✅', '❌', '> [!NOTE]', '> **Important:**', '> [!IMPORTANT]', '> **Note**:',
    '|---|---|---|', '|---|---|---|---|', '|---|---|', '|---|---|---|---|---|',
    'PLACEMENT_TYPE_NORMAL', 'APP_PROMOTION', 'WEBSITE', 'CATALOG', '["PLACEMENT_TIKTOK"]',
    'LEAD_GENERATION', 'WEB_CONVERSIONS', 'SINGLE_VIDEO', 'APP_INSTALL', 'TRAFFIC', 'ENGAGEMENT',
    'TIKTOK', 'TIKTOK_SHOP', 'PRODUCT_SALES', 'OFFLINE', 'STORE', 'LIVE_SHOPPING'
}

true_remaining = [l for l in remaining_en if l not in tech_markers and not re.match(r'^[A-Z0-9_\[\]",\s\.\-]+$', l)]

c_true = Counter(true_remaining)
print(f"Total true remaining prose lines: {len(true_remaining)} (unique: {len(c_true)})")

print("\n--- TOP 50 TRUE REMAINING PROSE LINES ---")
for l, cnt in c_true.most_common(50):
    print(f"[{cnt:2d}x] {l[:110]}")

import json
with open('tiktok-business-api/_work/true_remaining_after_master.json', 'w', encoding='utf-8') as f:
    json.dump([{"line": l, "count": cnt} for l, cnt in c_true.most_common()], f, ensure_ascii=False, indent=2)
