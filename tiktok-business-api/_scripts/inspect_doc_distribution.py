#!/usr/bin/env python3
import json
import re

with open('tiktok-business-api/_work/all_1501_en_lines.json') as f:
    items = json.load(f)

print(f"Total untranslated items in all_1501_en_lines.json: {len(items)}")

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

# Map doc_id to lines
c4_lines = []
c5_lines = []
c6_lines = []
other_lines = []

for item in items:
    did = item.get('doc_id')
    if did in cluster4_ids:
        c4_lines.append(item)
    elif did in cluster5_ids:
        c5_lines.append(item)
    elif did in cluster6_ids:
        c6_lines.append(item)
    else:
        other_lines.append(item)

print(f"Cluster 4 lines: {len(c4_lines)}")
print(f"Cluster 5 lines: {len(c5_lines)}")
print(f"Cluster 6 lines: {len(c6_lines)}")
print(f"Other lines (cluster 1-3 or unmapped): {len(other_lines)}")
