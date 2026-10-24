#!/usr/bin/env python3
import json, re, sys
sys.path.insert(0, 'tiktok-business-api/_scripts')

from part3_chunk1 import PART3_CHUNK1
from part3_chunk2 import PART3_CHUNK2
from part3_chunk3 import PART3_CHUNK3
from part3_chunk4 import PART3_CHUNK4

with open('tiktok-business-api/_work/part3_to_translate.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

merged_chunks = {}
merged_chunks.update(PART3_CHUNK1)
merged_chunks.update(PART3_CHUNK2)
merged_chunks.update(PART3_CHUNK3)
merged_chunks.update(PART3_CHUNK4)

print(f"Total items in Part 3 input: {len(items)}")
print(f"Total items in merged chunks: {len(merged_chunks)}")
assert len(items) == len(merged_chunks) == 200

part3_translated = []
for it in items:
    idx = it['index']
    assert idx in merged_chunks, f"Missing index {idx}"
    translated = merged_chunks[idx]
    part3_translated.append({
        'index': idx,
        'count': it['count'],
        'original': it['original'],
        'translated': translated
    })

with open('tiktok-business-api/_work/part3_translated.json', 'w', encoding='utf-8') as f:
    json.dump(part3_translated, f, ensure_ascii=False, indent=2)

print("Saved tiktok-business-api/_work/part3_translated.json successfully.")

# Verification of translated lines
en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)

suspicious = []
for it in part3_translated:
    s = it['translated']
    # remove inline code, markdown links target, URLs, known safe terms
    s = re.sub(r'\`[^\`]+\`', '', s)
    s = re.sub(r'\]\([^\)]+\)', ']', s)
    s = re.sub(r'https?://\S+', '', s)
    s = re.sub(r'\b[Aa]n\s+toàn\b', '', s)
    s = re.sub(r'\b[Ll]ý\s+do\b', '', s)
    s = re.sub(r'\b[Dd]o\s+(?:đó|vậy)\b', '', s)
    s = re.sub(r'\b[Ss]o\s+với\b', '', s)
    s = re.sub(r'\b[Kk]/[Dd]\b', '', s)
    matches = en_word_re.findall(s)
    if len(matches) >= 2:
        suspicious.append((it['index'], matches, it['translated'][:100]))

print(f"Suspicious remaining English in Part 3: {len(suspicious)}")
for idx, m, t in suspicious[:10]:
    print(f"  IDX {idx} (matches {m}): {t}")
