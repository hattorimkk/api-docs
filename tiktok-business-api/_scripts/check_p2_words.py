#!/usr/bin/env python3
import re
from collections import Counter
with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p2.md') as f:
    txt = f.read()
parts = txt.split('```')
prose = '\n'.join([parts[k] for k in range(0, len(parts), 2)])
en_words = re.findall(r'\b[A-Za-z]{4,}\b', prose)
allowed = {
    'tiktok', 'curl', 'post', 'json', 'http', 'https', 'true', 'false', 'null', 'none',
    'objective_type', 'campaign_type', 'budget_mode', 'budget', 'advertiser_id', 'campaign_name',
    'adgroup_name', 'optimization_goal', 'billing_event', 'bid_type', 'bid_price', 'pixel_id'
}
untrans = [w for w in en_words if w.lower() not in allowed]
counts = Counter(w.lower() for w in untrans)
print("Top 50 words in p2:")
for w, c in counts.most_common(50):
    print(f"{w}: {c}")
