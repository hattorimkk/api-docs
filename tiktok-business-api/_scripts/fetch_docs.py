#!/usr/bin/env python3
"""Tải toàn bộ docs TikTok Business API v1.3 (tiếng Anh) về dạng thô.

Nguồn: endpoint nội bộ mà trang portal dùng để render docs.
Kết quả:
  _raw/tree.json            cây mục lục
  _raw/index.json           danh sách phẳng (doc_id, title, path, depth, ...)
  _raw/docs/<doc_id>.json   nội dung mỗi tài liệu
Có thể chạy lại: tài liệu đã tải sẽ được bỏ qua.
"""
import json, os, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://business-api.tiktok.com/gateway/api/doc/client"
KEY = "c0138ffadd90a955c1f0670a56fe348d1d40680b3c89461e09f78ed26785164b"  # v1.3
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_raw")
DOCS = os.path.join(ROOT, "docs")
os.makedirs(DOCS, exist_ok=True)


def get(url, tries=5):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa
            time.sleep(1.5 * (i + 1))
            err = e
    raise err


def fetch_tree():
    p = os.path.join(ROOT, "tree.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    q = urllib.parse.urlencode({"identify_key": KEY, "language": "ENGLISH", "isNeedContent": "false"})
    d = get(f"{BASE}/platform/tree/get/?{q}")
    assert d["code"] == 0, d
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    return d


def flatten(nodes, path=(), depth=0, out=None):
    out = [] if out is None else out
    for n in nodes:
        p = path + (n["title"].strip(),)
        out.append({"doc_id": str(n["doc_id"]), "title": n["title"].strip(), "path": list(p),
                    "depth": depth, "parent_id": str(n["parent_id"]), "n_children": len(n.get("child_docs", []))})
        flatten(n.get("child_docs", []), p, depth + 1, out)
    return out


def fetch_doc(doc_id):
    f = os.path.join(DOCS, f"{doc_id}.json")
    if os.path.exists(f) and os.path.getsize(f) > 0:
        return doc_id, "skip"
    q = urllib.parse.urlencode({"identify_key": KEY, "doc_id": doc_id, "language": "ENGLISH"})
    d = get(f"{BASE}/node/get/v2/?{q}")
    if d.get("code") != 0:
        return doc_id, f"ERR {d.get('code')} {d.get('msg')}"
    json.dump(d["data"], open(f, "w", encoding="utf-8"), ensure_ascii=False)
    return doc_id, "ok"


def main():
    tree = fetch_tree()
    flat = flatten(tree["data"]["primary_doc_list"])
    json.dump(flat, open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("tổng số tài liệu:", len(flat), flush=True)
    done = errs = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(fetch_doc, x["doc_id"]) for x in flat]
        for fu in as_completed(futs):
            try:
                did, st = fu.result()
            except Exception as e:  # noqa
                did, st = "?", f"EXC {e}"
            done += 1
            if st.startswith(("ERR", "EXC")):
                errs += 1
                print(did, st, flush=True)
            if done % 50 == 0:
                print(f"{done}/{len(flat)} (lỗi: {errs})", flush=True)
    print("xong", done, "lỗi", errs, flush=True)


if __name__ == "__main__":
    main()

