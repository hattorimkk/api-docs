#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/untouched_after_c3.json') as f:
    items = json.load(f)

# Pure technical / markdown constants
def is_technical_or_format(line):
    s = line.strip()
    if s in ['N/A', '✅', '❌', '> [!NOTE]', '> **Important:**', '> [!IMPORTANT]', '> **Note**:']:
        return True
    if re.match(r'^\|[\-\|\s:]+\|$', s): # table separator
        return True
    if re.match(r'^[A-Z0-9_\[\]",\s\.\-]+$', s): # ALL_CAPS constant
        return True
    return False

prose_untrans = [it for it in items if not is_technical_or_format(it['orig'])]

print(f"Total untouched items: {len(items)}")
print(f"Real prose/text items needing translation: {len(prose_untrans)}")

with open('tiktok-business-api/_work/real_prose_untouched.json', 'w', encoding='utf-8') as f:
    json.dump(prose_untrans, f, ensure_ascii=False, indent=2)

print("\n--- SAMPLE REAL PROSE UNTOUCHED (first 30) ---")
for it in prose_untrans[:30]:
    print(f"[{it['count']:2d}x] {it['orig'][:110]}")
