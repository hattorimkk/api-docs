#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/all_residual_sentences.json') as f:
    items = json.load(f)

c1_3_dids = {
    '1758526151905281', '1782086026530817', '1782086386057218', '1782086858169345',
    '1782087093223425', '1782087227448322', '1782087289569282', '1782087310574594',
    '1782087361715201', '1782087383794690', '1782087405206530', '1782087440474113',
    '1782087462002690', '1782087508216834', '1741942179356738', '1837161048383489',
    '1741942291730434', '1750361698613249', '1774519076905985', '1775099621140482',
    '1782087855154177', '1750361719059457', '1759232259360770', '1754162402455554',
    '1785886237030401', '1754726939130882', '1742003478618114'
}

p2_items = [it for it in items if it['doc_id'] in c1_3_dids]
p3_items = [it for it in items if it['doc_id'] not in c1_3_dids]

with open('tiktok-business-api/_work/residual_p2.json', 'w', encoding='utf-8') as f:
    json.dump(p2_items, f, ensure_ascii=False, indent=2)

with open('tiktok-business-api/_work/residual_p3.json', 'w', encoding='utf-8') as f:
    json.dump(p3_items, f, ensure_ascii=False, indent=2)

print("Saved residual_p2.json and residual_p3.json")
