import re

txt = open("tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md").read()
matches = list(re.finditer(r"<a id=\"doc-(\d+)\"></a>", txt))

for i, m in enumerate(matches):
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(txt)
    doc_id = m.group(1)
    doc_chunk = txt[start:end]
    bc = [l for l in doc_chunk.splitlines() if l.startswith("> Đường dẫn:")]
    if bc:
        print(f"'{doc_id}': '{bc[0]}',")
