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

vi_re = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]|\b(trang|web|quang|cao|chien|dich|nhom|cai|dat|yeu|cau|tham|so|danh|muc)\b', re.IGNORECASE)
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
    'TikTok', 'TikTok Shop', 'Pixel', 'oCPM', '18+', 'App', '* TikTok Business Center'
}

true_untrans = [l for l in remaining_en if l not in tech_markers and not re.match(r'^[A-Z0-9_\[\]",\s\.\-]+$', l)]

c = Counter(true_untrans)
print(f"Total true untranslated lines: {len(true_untrans)} (unique: {len(c)})")

import json
with open('tiktok-business-api/_work/final_untrans_lines.json', 'w', encoding='utf-8') as f:
    json.dump([{"line": l, "count": cnt} for l, cnt in c.most_common()], f, ensure_ascii=False, indent=2)

print("\n--- SAMPLE OF REMAINING UNTRANSLATED (first 40) ---")
for l, cnt in c.most_common(40):
    print(f"[{cnt:2d}x] {l[:100]}")
