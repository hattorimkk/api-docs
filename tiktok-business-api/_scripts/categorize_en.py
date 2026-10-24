import re

lines = open("tiktok-business-api/_work/u101_en_lines.txt").read().splitlines()
headings = [l for l in lines if l.startswith("#")]
quotes = [l for l in lines if l.startswith(">")]
tables = [l for l in lines if l.startswith("|")]
lists = [l for l in lines if re.match(r"^(\-|\*|\d+\.)", l)]
others = [l for l in lines if not (l.startswith("#") or l.startswith(">") or l.startswith("|") or re.match(r"^(\-|\*|\d+\.)", l))]

print(f"Headings: {len(headings)}")
print(f"Quotes: {len(quotes)}")
print(f"Pipe tables: {len(tables)}")
print(f"Lists: {len(lists)}")
print(f"Others (prose / 4-line table cells): {len(others)}")
