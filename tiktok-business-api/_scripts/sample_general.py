import os
import re

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

pure_lines = [l.split("\t", 1)[1] for l in open(os.path.join(ROOT, "_work/pure_en.txt")).read().splitlines()]

creatives = set([l for l in pure_lines if any(k in l.lower() for k in ["creative", "video", "image", "carousel", "music", "identity", "spark"])])
bidding = set([l for l in pure_lines if any(k in l.lower() for k in ["budget", "bid", "optimization", "roas", "cpa", "cbo", "conversion", "pixel", "event"])])
catalog = set([l for l in pure_lines if any(k in l.lower() for k in ["catalog", "product", "feed", "shop", "store", "commerce", "seller", "inventory"])])
targeting = set([l for l in pure_lines if any(k in l.lower() for k in ["targeting", "audience", "placement", "pangle", "location", "country", "age", "gender"])])
general = [l for l in pure_lines if l not in creatives and l not in bidding and l not in catalog and l not in targeting]

for l in general[:50]:
    print("---", l[:120])
