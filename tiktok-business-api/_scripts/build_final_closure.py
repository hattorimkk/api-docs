#!/usr/bin/env python3
"""
Inspect all remaining lines and build the final closure dictionary.
"""
import json

with open('tiktok-business-api/_work/final_untrans_lines.json') as f:
    items = json.load(f)

print(f"Total lines to translate in closure: {len(items)}")

# We will construct a mapping of exact line -> translated line
# Let's write out a script that defines FINAL_CLOSURE_RULES
