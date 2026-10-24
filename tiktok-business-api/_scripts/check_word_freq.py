#!/usr/bin/env python3
import os, sys, re
from collections import Counter
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
from inspect_remaining_u101 import new_text

parts = new_text.split('```')
prose = '\n'.join([parts[k] for k in range(0, len(parts), 2)])
en_words = re.findall(r'\b[A-Za-z]{3,}\b', prose)
allowed = {
    'tiktok', 'curl', 'post', 'json', 'http', 'https', 'true', 'false', 'null', 'none',
    'objective_type', 'campaign_type', 'budget_mode', 'budget', 'advertiser_id', 'campaign_name',
    'adgroup_name', 'optimization_goal', 'billing_event', 'bid_type', 'bid_price', 'pixel_id'
}
untrans = [w for w in en_words if w.lower() not in allowed]
counts = Counter(w.lower() for w in untrans)
print('Total untranslated word tokens:', len(untrans))
print('Unique untranslated words:', len(counts))
print('Top 50 untranslated words:')
for w, c in counts.most_common(50):
    print(f'{w}: {c}')
