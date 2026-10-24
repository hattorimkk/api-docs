import re

with open("tiktok-business-api/docs/09-marketing-api/do-luong-quang-cao-tom-tat.md", "r", encoding="utf-8") as f:
    text = f.read()

docs = re.split(r'(?=<a id="doc-\d+"></a>)', text)
VI_RE = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')

def get_doc_en_lines(doc_indices):
    lines_found = []
    for di in doc_indices:
        d = docs[di]
        in_code = False
        for l in d.splitlines():
            raw = l.strip()
            if raw.startswith("```"):
                in_code = not in_code
                continue
            if in_code or not raw or raw.startswith("|") or raw.startswith("<!--") or raw.startswith("<a id=") or raw.startswith("---"):
                continue
            clean = re.sub(r'\[.*?\]\(.*?\)', '', raw)
            clean = re.sub(r'`.*?`', '', clean)
            clean = re.sub(r'https?://\S+', '', clean)
            clean = re.sub(r'#+\s*', '', clean)
            words = re.findall(r'\b[A-Za-z]{2,}\b', clean)
            if not VI_RE.search(raw) and len(words) >= 3:
                lines_found.append(raw)
    return list(dict.fromkeys(lines_found))

sec_a = get_doc_en_lines(range(1, 7))
sec_b = get_doc_en_lines([7, 8, 9])
sec_c = get_doc_en_lines([10, 11, 12, 13])
sec_d = get_doc_en_lines([14, 15])
sec_e = get_doc_en_lines([16, 17, 18])

print(f"Sec A (Docs 1-6): {len(sec_a)}")
print(f"Sec B (Docs 7-9): {len(sec_b)}")
print(f"Sec C (Docs 10-13): {len(sec_c)}")
print(f"Sec D (Docs 14-15): {len(sec_d)}")
print(f"Sec E (Docs 16-18): {len(sec_e)}")

for name, sec in [("a", sec_a), ("b", sec_b), ("c", sec_c), ("d", sec_d), ("e", sec_e)]:
    with open(f"/tmp/sec_{name}.txt", "w", encoding="utf-8") as out:
        for l in sec:
            out.write(l + "\n")
