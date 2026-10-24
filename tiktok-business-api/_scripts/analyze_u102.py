with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p2.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('```')
prose = '\n'.join([parts[i] for i in range(0, len(parts), 2)])

lines = [l.strip() for l in prose.splitlines() if l.strip() and not l.strip().startswith('<') and not l.strip().startswith('<!--')]

import re

untranslated_lines = []
for l in lines:
    cleaned = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', l)
    cleaned = re.sub(r'`[^`]+`', '', cleaned)
    cleaned = re.sub(r'\([^\)]*\)', '', cleaned)
    cleaned = cleaned.replace('|', ' ').replace('-', ' ').strip()
    words = re.findall(r'\b[A-Za-z]{3,}\b', cleaned)
    en_words = [w for w in words if w.lower() not in ('cho', 'cac', 'cua', 'nay', 'luc', 'muc', 'nam', 'qua', 'tai', 'vao', 'bao', 'gia', 'ban', 'ten', 'sau', 'day', 'don', 'tam', 'chi', 'can', 'khi', 'xem', 'voi', 'theo', 'nhom', 'dich', 'viet', 'bang', 'kho', 'dong', 'hang', 'tuc', 'thoi', 'trang', 'diem', 'nguon', 'tinh', 'huong', 'dung', 'buoc', 'thuc', 'hien', 'phu', 'luc', 'dieu', 'kien', 'tien', 'quyet', 'thao', 'tac', 'tra', 'cuu', 'thong', 'tin', 'ma', 'lenh', 'mau', 'goi', 'phan', 'hoi', 'ghi', 'chu', 'luu', 'loai', 'hinh', 'sang', 'tao', 'danh', 'sach', 'chuyen', 'doi', 'doanh', 'nghiep', 'khach', 'tiem', 'nang', 'ung', 'toan', 'dien', 'nang', 'cap')]
    if en_words:
        untranslated_lines.append((l, en_words))

from collections import Counter
c = Counter([x[0] for x in untranslated_lines])

print("All untranslated lines with count >= 8:")
for l, cnt in c.most_common(100):
    if cnt >= 8:
        print(f"[{cnt}x] {repr(l)}")
