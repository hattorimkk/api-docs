#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/residual_p2.json') as f:
    items = json.load(f)

print(f"Total items in residual_p2: {len(items)}")
for i, it in enumerate(items[:20]):
    print(f"{i+1}. [{it['doc_id']}] {it['line'][:100]}")
