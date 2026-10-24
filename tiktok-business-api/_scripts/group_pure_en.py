import os
import re

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

pure_lines = [l.split("\t", 1)[1] for l in open(os.path.join(ROOT, "_work/pure_en.txt")).read().splitlines()]

# Theme 1: Ad creatives, formats, and assets
creatives = [l for l in pure_lines if any(k in l.lower() for k in ["creative", "video", "image", "carousel", "music", "identity", "spark"])]
# Theme 2: Budget, bidding, optimization goal, events
bidding = [l for l in pure_lines if any(k in l.lower() for k in ["budget", "bid", "optimization", "roas", "cpa", "cbo", "conversion", "pixel", "event"])]
# Theme 3: Catalog, products, shop, commerce
catalog = [l for l in pure_lines if any(k in l.lower() for k in ["catalog", "product", "feed", "shop", "store", "commerce", "seller", "inventory"])]
# Theme 4: Targeting, audience, location, placement
targeting = [l for l in pure_lines if any(k in l.lower() for k in ["targeting", "audience", "placement", "pangle", "location", "country", "age", "gender"])]
# Theme 5: Instructions, prerequisites, docs
general = [l for l in pure_lines if l not in creatives and l not in bidding and l not in catalog and l not in targeting]

print(f"Creatives: {len(creatives)}")
print(f"Bidding: {len(bidding)}")
print(f"Catalog: {len(catalog)}")
print(f"Targeting: {len(targeting)}")
print(f"General/Others: {len(general)}")
