import os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)
pure_lines = [l.split("\t", 1)[1] for l in open(os.path.join(ROOT, "_work/pure_en.txt")).read().splitlines()]
catalog = [l for l in pure_lines if any(k in l.lower() for k in ["catalog", "product", "feed", "shop", "store", "commerce", "seller", "inventory"])]
targeting = [l for l in pure_lines if any(k in l.lower() for k in ["targeting", "audience", "placement", "pangle", "location", "country", "age", "gender"])]
print("--- CATALOG (first 25) ---")
for l in catalog[:25]:
    print("---", l[:120])
print("\n--- TARGETING (first 25) ---")
for l in targeting[:25]:
    print("---", l[:120])
