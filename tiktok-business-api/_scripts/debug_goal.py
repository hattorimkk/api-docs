import re
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

text = open(os.path.join(ROOT, "docs/08-use-cases/use-case-tao-chien-dich-p1.md"), encoding="utf-8").read()

idx = text.find("Optimization and bidding · Goal")
if idx != -1:
    print(repr(text[idx:idx+500]))
else:
    print("Not found exact 'Optimization and bidding · Goal'")
    idx2 = text.find("Mục tiêu (Goal)")
    print(repr(text[idx2:idx2+500]))
