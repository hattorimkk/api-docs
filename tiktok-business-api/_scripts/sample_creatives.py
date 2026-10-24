import os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)
pure_lines = [l.split("\t", 1)[1] for l in open(os.path.join(ROOT, "_work/pure_en.txt")).read().splitlines()]
creatives = [l for l in pure_lines if any(k in l.lower() for k in ["creative", "video", "image", "carousel", "music", "identity", "spark"])]
for l in creatives[:50]:
    print("---", l[:120])
