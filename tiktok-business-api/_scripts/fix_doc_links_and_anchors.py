#!/usr/bin/env python3
"""
Sửa toàn diện và triệt để các liên kết tài liệu trong tiktok-business-api:
1. Thêm thẻ anchor <a id="doc-{did}"></a> trước các comment <!-- doc_id: {did} --> chưa có anchor.
2. Thay thế toàn bộ liên kết [Tên](slug:{slug_name}) thành [Tên]({relative_path}#doc-{did}).
3. Sửa link ảnh (//images.ctfassets.net/...) thành (https://images.ctfassets.net/...).
4. Xử lý các link [doc:{did}] còn sót lại.
"""

import os
import glob
import re
import json
import sys

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_idx_path = os.path.join(base_dir, '_raw', 'index.json')
    units_path = os.path.join(base_dir, '_work', 'units.json')

    with open(raw_idx_path, 'r', encoding='utf-8') as f:
        raw_idx = json.load(f)

    with open(units_path, 'r', encoding='utf-8') as f:
        units = json.load(f)

    # 1. slug -> doc_id
    slug_to_doc = {}
    for item in raw_idx:
        s = item.get('slug')
        did = str(item.get('doc_id'))
        if s:
            slug_to_doc[s] = did

    # Thêm aliases / fallback cho các slug chưa có trong raw_idx hoặc cần điều hướng chuẩn
    slug_to_doc['get-upgraded-smart-material-report-overview'] = '1843317489576961'
    slug_to_doc['ad-account-status'] = '1737174886619138'
    slug_to_doc['get-upgraded-smart-creatives'] = '1843317378982914'
    slug_to_doc['location-ids'] = '1737172315193346'
    slug_to_doc['api-reference'] = '1735712062490625'

    # 2. doc_id -> target_file (tương đối so với base_dir)
    doc_to_file = {}
    for u in units:
        out = u['out']
        for did in u['doc_ids']:
            doc_to_file[str(did)] = out

    doc_to_file['1737172315193346'] = 'docs/phu-luc/phu-luc-p1.md'
    doc_to_file['1735712062490625'] = 'docs/tong-quan/tong-quan-va-phien-ban.md'
    doc_to_file['1829744071179330'] = 'docs/api-reference/63-spark-ads-recommendation.md'
    doc_to_file['1771101303285761'] = 'docs/api-reference/42-events-2-0.md'
    doc_to_file['1768506960432130'] = 'docs/organic-api/tiktok-one-api.md'
    doc_to_file['1825117875361793'] = 'docs/organic-api/tiktok-one-api.md'
    doc_to_file['1738373141733378'] = 'docs/huong-dan/marketing-api-xac-thuc-uy-quyen.md'
    doc_to_file['1738083939371009'] = 'docs/organic-api/accounts-api.md'

    # Sửa lỗi dòng thừa doc_id: 1876678060056257 trong docs/mcp/mcp-server-tom-tat.md
    mcp_tomtat_path = os.path.join(base_dir, 'docs/mcp/mcp-server-tom-tat.md')
    if os.path.exists(mcp_tomtat_path):
        with open(mcp_tomtat_path, 'r', encoding='utf-8') as f:
            mcp_txt = f.read()
        mcp_bad_pattern = "<!-- doc_id: 1876678060056257 -->\n<!-- doc_id: 1876677898348545 -->"
        if mcp_bad_pattern in mcp_txt:
            mcp_txt = mcp_txt.replace(mcp_bad_pattern, "<!-- doc_id: 1876677898348545 -->")
            with open(mcp_tomtat_path, 'w', encoding='utf-8') as f:
                f.write(mcp_txt)
            print("Đã tinh chỉnh marker thừa trong docs/mcp/mcp-server-tom-tat.md")

    # Lấy danh sách toàn bộ file markdown mục tiêu
    md_files = sorted(glob.glob(os.path.join(base_dir, 'docs/**/*.md'), recursive=True) + [os.path.join(base_dir, 'README.md')])

    stats = {
        'total_files': len(md_files),
        'files_modified': 0,
        'anchors_added': 0,
        'slug_links_replaced': 0,
        'ctf_links_fixed': 0,
        'doc_links_fixed': 0
    }

    for filepath in md_files:
        file_dir = os.path.dirname(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        orig_content = content

        # Bước 1: Thêm thẻ anchor <a id="doc-{did}"></a>
        lines = content.split('\n')
        new_lines = []
        file_anchors = 0
        for idx, line in enumerate(lines):
            m = re.match(r'^\s*<!--\s*doc_id:\s*(\d+)\s*-->\s*$', line)
            if m:
                did = m.group(1)
                anchor_tag = f'<a id="doc-{did}"></a>'
                prev_line = new_lines[-1] if new_lines else ''
                prev_2 = new_lines[-2] if len(new_lines) >= 2 else ''
                if prev_line != anchor_tag and prev_2 != anchor_tag:
                    new_lines.append(anchor_tag)
                    file_anchors += 1
            new_lines.append(line)

        stats['anchors_added'] += file_anchors
        content = '\n'.join(new_lines)

        # Bước 2: Thay thế [Tên](slug:{slug_name}) thành [Tên]({rel_path}#doc-{did})
        def repl_slug(match):
            text = match.group(1)
            slug_raw = match.group(2)
            slug_clean = slug_raw.split('#')[0]
            if slug_clean in slug_to_doc:
                did = slug_to_doc[slug_clean]
                if did in doc_to_file:
                    target_out = doc_to_file[did]
                    target_abs = os.path.join(base_dir, target_out)
                    rel_path = os.path.relpath(target_abs, file_dir)
                    stats['slug_links_replaced'] += 1
                    return f'[{text}]({rel_path}#doc-{did})'
                else:
                    print(f"Cảnh báo: did {did} từ slug {slug_clean} không có target file", file=sys.stderr)
            else:
                print(f"Cảnh báo: slug {slug_clean} không tồn tại trong map", file=sys.stderr)
            return match.group(0)

        content = re.sub(r'\[([^\]]*)\]\(slug:([^)]+)\)', repl_slug, content)

        # Bước 3: Sửa link ảnh ctfassets
        content, ctf_count = re.subn(r'\(//images\.ctfassets\.net/', r'(https://images.ctfassets.net/', content)
        stats['ctf_links_fixed'] += ctf_count

        # Bước 4: Sửa các link doc: còn sót lại
        if 'marketing-api-xac-thuc-uy-quyen.md' in filepath:
            # Sửa các reference TTCM và các doc ID trong bảng xác thực
            content = content.replace('[doc:1781189065082881]', '[TTCM Authorization](https://business-api.tiktok.com/portal/docs?id=1781189065082881)')
            content = content.replace('[doc:1768506960432130]', '[Ủy quyền Creator](../organic-api/tiktok-one-api.md#doc-1768506960432130)')
            content = content.replace('[doc:1825117875361793]', '[Ủy quyền TTO](../organic-api/tiktok-one-api.md#doc-1825117875361793)')
            content = content.replace('[doc:1738373141733378]', '[Ủy quyền Marketing API](#doc-1738373141733378)')
            content = content.replace('[doc:1738083939371009]', '[Ủy quyền Accounts API](../organic-api/accounts-api.md#doc-1738083939371009)')
            stats['doc_links_fixed'] += 7

        if '63-spark-ads-recommendation.md' in filepath:
            content = content.replace('` [doc:1829744071179330])', '` [chi tiết](#doc-1829744071179330))')
            stats['doc_links_fixed'] += 1

        if '43-events-1-0-p1.md' in filepath:
            content = content.replace(' - [doc:1771101303285761])', ' - [xem tài liệu](42-events-2-0.md#doc-1771101303285761))')
            stats['doc_links_fixed'] += 1

        if content != orig_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            stats['files_modified'] += 1

    print("=== KẾT QUẢ THỰC THI ===")
    print(f"Tổng số file markdown duyệt qua: {stats['total_files']}")
    print(f"Số file đã cập nhật: {stats['files_modified']}")
    print(f"Số thẻ anchor <a id=\"doc-...\"> đã thêm: {stats['anchors_added']}")
    print(f"Số liên kết slug: đã thay thế thành công: {stats['slug_links_replaced']}")
    print(f"Số liên kết ảnh ctfassets đã sửa sang https: {stats['ctf_links_fixed']}")
    print(f"Số liên kết doc: lẻ đã chuẩn hóa: {stats['doc_links_fixed']}")

if __name__ == '__main__':
    main()
