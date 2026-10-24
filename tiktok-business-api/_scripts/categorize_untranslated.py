#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    full_text = f.read()

# Split into docs
docs = re.split(r'(?=<a id="doc-\d+"></a>)', full_text)
doc_map = {}
for d in docs:
    m = re.search(r'<a id="doc-(\d+)"></a>', d)
    if m:
        did = m.group(1)
        doc_map[did] = d

with open('tiktok-business-api/_work/real_prose_untouched.json') as f:
    items = json.load(f)

cluster4_ids = {
    '1758528372513794', '1822009058467842', '1822009220448257', '1822009242546258',
    '1768006268820546', '1827645480080385', '1814122471133186', '1814122492598274'
}

cluster5_ids = {
    '1843309449749698', '1843309500205058', '1853377390815233', '1853377803841537',
    '1875231879602658', '1875231912916994', '1875231953230418', '1879220213492353',
    '1868120855134226', '1868121865281538', '1853377811982657', '1863331595515009'
}

cluster6_ids = {
    '1843309514567809', '1847302878676994', '1847302895272962', '1847302908327938',
    '1847302920924306', '1847302935967746'
}

categorized = {
    "c4": [],
    "c5": [],
    "c6": [],
    "other_or_common": []
}

for it in items:
    orig = it['orig']
    # find where orig appears
    matched_clusters = set()
    for did, dtext in doc_map.items():
        if orig in dtext:
            if did in cluster4_ids:
                matched_clusters.add('c4')
            elif did in cluster5_ids:
                matched_clusters.add('c5')
            elif did in cluster6_ids:
                matched_clusters.add('c6')
            else:
                matched_clusters.add('other')
                
    it['matched_clusters'] = list(matched_clusters)
    if 'c4' in matched_clusters and len(matched_clusters) == 1:
        categorized['c4'].append(it)
    elif 'c5' in matched_clusters and len(matched_clusters) == 1:
        categorized['c5'].append(it)
    elif 'c6' in matched_clusters and len(matched_clusters) == 1:
        categorized['c6'].append(it)
    else:
        categorized['other_or_common'].append(it)

print(f"C4-only items: {len(categorized['c4'])}")
print(f"C5-only items: {len(categorized['c5'])}")
print(f"C6-only items: {len(categorized['c6'])}")
print(f"Multi-cluster or other items: {len(categorized['other_or_common'])}")

with open('tiktok-business-api/_work/categorized_untranslated.json', 'w', encoding='utf-8') as f:
    json.dump(categorized, f, ensure_ascii=False, indent=2)
