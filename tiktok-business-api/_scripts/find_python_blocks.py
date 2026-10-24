import glob, re

files_with_python = []
for f in sorted(glob.glob('docs/**/*.md', recursive=True)):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    matches = len(re.findall(r'```python', txt))
    if matches > 0:
        files_with_python.append((f, matches))

print(f"Số file còn code block Python: {len(files_with_python)}")
for f, m in files_with_python:
    print(f"  {f}: {m} python blocks")

