#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/true_remaining_after_master.json') as f:
    items = json.load(f)

# Sort into categories:
# 1. Short labels (<= 3 words)
# 2. Sentences (> 3 words)
short_labels = []
sentences = []

for it in items:
    l = it['line']
    words = l.split()
    if len(words) <= 3:
        short_labels.append(it)
    else:
        sentences.append(it)

print(f"Total items: {len(items)}")
print(f"Short labels (<= 3 words): {len(short_labels)}")
print(f"Sentences (> 3 words): {len(sentences)}")

with open('tiktok-business-api/_work/residual_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences, f, ensure_ascii=False, indent=2)

with open('tiktok-business-api/_work/residual_short_labels.json', 'w', encoding='utf-8') as f:
    json.dump(short_labels, f, ensure_ascii=False, indent=2)

print("\n--- SAMPLE SHORT LABELS (first 25) ---")
for it in short_labels[:25]:
    print(f"[{it['count']:2d}x] {repr(it['line'])}")

print("\n--- SAMPLE SENTENCES (first 25) ---")
for it in sentences[:25]:
    print(f"[{it['count']:2d}x] {repr(it['line'][:100])}")
