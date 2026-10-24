import os, re, json, glob

base_dir = '/Users/hattorimk/Desktop/api-docs/tiktok-business-api'
units_path = os.path.join(base_dir, '_work/units.json')
units = json.load(open(units_path))

# 1. Xây dựng bản đồ doc_id -> out_file
doc_map = {}
for u in units:
    out = u['out']
    for doc_id in u['doc_ids']:
        doc_map[str(doc_id)] = out

print(f"Loaded {len(doc_map)} doc_ids mapped to files.")

# 2. Quét và thay thế trong tất cả file markdown
md_files = glob.glob(os.path.join(base_dir, 'docs/**/*.md'), recursive=True)
md_files += glob.glob(os.path.join(base_dir, '*.md'))

pattern = re.compile(r'\[([^\]]+)\]\(doc:(\d+)\)')

stats = {'total_replaced': 0, 'files_updated': 0}

for filepath in md_files:
    if '_work' in filepath or '_clean' in filepath or '_raw' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    file_dir = os.path.dirname(filepath)

    def replacer(match):
        text = match.group(1)
        doc_id = match.group(2)
        stats['total_replaced'] += 1
        if doc_id in doc_map:
            target_out = doc_map[doc_id]
            target_abs = os.path.join(base_dir, target_out)
            rel_path = os.path.relpath(target_abs, file_dir)
            return f"[{text}]({rel_path}#doc-{doc_id})"
        else:
            return f"**{text}**"

    new_content = pattern.sub(replacer, content)
    new_content = re.sub(r'\(doc:(\d+)\)', r'(#doc-\1)', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        stats['files_updated'] += 1

print(f"Updated {stats['files_updated']} files, replaced {stats['total_replaced']} doc links.")

