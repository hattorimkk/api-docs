import re

lines = open("tiktok-business-api/_work/u101_to_translate.txt").read().splitlines()

# Let's inspect breadcrumbs
breadcrumbs = [l for l in lines if "> Đường dẫn:" in l or "> Path:" in l]
print(f"Breadcrumb lines: {len(breadcrumbs)}")
for b in breadcrumbs[:10]:
    print(" ", b)

# Let's inspect TOC lines
toc = [l for l in lines if re.match(r"^\s*\d+\s*\- \[\d+\.", l) or re.match(r"^\- \[\d+\.", l)]
print(f"\nTOC lines: {len(toc)}")
for t in toc[:10]:
    print(" ", t)

# Let's inspect headings
h = [l for l in lines if l.startswith("#") or re.match(r"^\s*\d+\s*#", l)]
print(f"\nHeading lines: {len(h)}")
for x in h[:15]:
    print(" ", x)
