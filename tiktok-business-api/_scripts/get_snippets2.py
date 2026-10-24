import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

from test_engine import new_text

parts = new_text.split("```")
prose = "\n".join([parts[i] for i in range(0, len(parts), 2)])

def find_snippet(keyword, length=1200):
    idx = prose.find(keyword)
    if idx != -1:
        print(f"=== SNIPPET FOR: {keyword} ===")
        print(prose[idx:idx+length])
        print("\n" + "="*50 + "\n")

find_snippet("Specify a TikTok Shop that is available for")
find_snippet("Promotion type and you can decide where you'd like to promote")
find_snippet("The list of Showcase products that you want to use")
find_snippet("Creating Tương tác cộng đồng (Community Interaction) ad groups with interaction type as Live")
