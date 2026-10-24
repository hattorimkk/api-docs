#!/usr/bin/env python3
"""Dựng manifest công việc dịch: _work/units/<unit_id>.json + _work/units.json
và các bản rút gọn _digest/<doc_id>.md cho tài liệu quá dài.
"""
import json, os, re, unicodedata

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CLEAN = os.path.join(ROOT, "_clean")
DIGEST = os.path.join(ROOT, "_digest")
UNITS = os.path.join(ROOT, "_work", "units")
os.makedirs(DIGEST, exist_ok=True)
os.makedirs(UNITS, exist_ok=True)
for f in os.listdir(UNITS):
    os.remove(os.path.join(UNITS, f))

idx = json.load(open(os.path.join(ROOT, "_raw", "index.json"), encoding="utf-8"))
by_id = {x["doc_id"]: x for x in idx}
MAX_CHARS = 170_000
DIGEST_THRESHOLD = 40_000  # tài liệu hướng dẫn dài hơn mức này -> digest

# ---- tên tiếng Việt của nhóm API Reference -------------------------------------------------
VI = {
 "Accounts": "Tài khoản TikTok (Accounts)", "Ads": "Quảng cáo (Ads)", "Ad Accounts": "Tài khoản quảng cáo (Ad Accounts)",
 "Ad Comments": "Bình luận quảng cáo (Ad Comments)", "Ad Comments - Blocked Words": "Từ khóa bị chặn trong bình luận (Blocked Words)",
 "Ad Diagnosis": "Chẩn đoán quảng cáo (Ad Diagnosis)", "Ad Groups": "Nhóm quảng cáo (Ad Groups)", "Ad Review": "Duyệt quảng cáo (Ad Review)",
 "Audience": "Tệp đối tượng (Audience)", "Authentication": "Xác thực (Authentication)", "Automated Rules": "Quy tắc tự động (Automated Rules)",
 "BC Management": "Quản lý Business Center (BC Management)", "BC Payments": "Thanh toán BC (BC Payments)",
 "BC Payment Portfolios": "Danh mục thanh toán BC (BC Payment Portfolios)", "BC Assets": "Tài sản BC (BC Assets)",
 "BC Asset Groups": "Nhóm tài sản BC (BC Asset Groups)", "BC Billing Groups": "Nhóm thanh toán BC (BC Billing Groups)",
 "BC Partners": "Đối tác BC (BC Partners)", "BC Members": "Thành viên BC (BC Members)", "BC Invoices": "Hóa đơn BC (BC Invoices)",
 "BC Reporting": "Báo cáo BC (BC Reporting)", "Brand Safety": "An toàn thương hiệu (Brand Safety)",
 "Business Messaging": "Tin nhắn doanh nghiệp (Business Messaging)", "Campaign": "Chiến dịch (Campaign)",
 "Catalog Management": "Quản lý Catalog", "Catalog Event Sources": "Nguồn sự kiện Catalog", "Catalog Feeds": "Feed Catalog",
 "Catalog Products": "Sản phẩm Catalog", "Catalog Product Sets": "Bộ sản phẩm Catalog", "Catalog Videos": "Video Catalog",
 "Catalog Video Templates": "Mẫu video Catalog", "Catalog Diagnostics": "Chẩn đoán Catalog", "Catalog Insights": "Insight Catalog",
 "Change Log": "Nhật ký thay đổi (Change Log)", "Creative Pre-review": "Tiền kiểm duyệt creative (Creative Pre-review)",
 "Creative Portfolios": "Danh mục creative (Creative Portfolios)", "Creative Reports": "Báo cáo creative (Creative Reports)",
 "Creative Tools": "Công cụ creative (Creative Tools)", "Custom Conversions": "Chuyển đổi tùy chỉnh (Custom Conversions)",
 "Discovery": "Khám phá (Discovery)", "(Deprecated) Dynamic Scene": "Dynamic Scene (đã ngừng hỗ trợ)", "Events 2.0": "Sự kiện 2.0 (Events 2.0)",
 "Events 1.0": "Sự kiện 1.0 (Events 1.0)", "Files": "Tệp (Files)", "GMV Max": "GMV Max", "Identity": "Danh tính (Identity)",
 "Images": "Hình ảnh (Images)", "Leads": "Khách hàng tiềm năng (Leads)", "Media Mix Modeling": "Media Mix Modeling (MMM)",
 "MCP Authorization": "Ủy quyền MCP (MCP Authorization)", "Mentions": "Lượt nhắc (Mentions)", "Music": "Âm nhạc (Music)",
 "Negative Keywords": "Từ khóa loại trừ (Negative Keywords)", "Page": "Trang đích (Page)", "Pangle": "Pangle", "Playable Ads": "Quảng cáo Playable (Playable Ads)",
 "Reach & Frequency": "Reach & Frequency", "Reporting": "Báo cáo (Reporting)", "Showcase": "Showcase", "Smart Creative": "Smart Creative",
 "(To be deprecated) Legacy Smart+": "Smart+ phiên bản cũ (sắp ngừng hỗ trợ)", "Upgraded Smart+": "Smart+ nâng cấp (Upgraded Smart+)",
 "Spark Ads Recommendation": "Gợi ý Spark Ads", "Spark Ads Using Authorized Posts": "Spark Ads từ bài đăng được ủy quyền",
 "Super Split Test": "Super Split Test", "Subscription": "Đăng ký webhook (Subscription)", "Terms": "Điều khoản (Terms)", "TikTok One": "TikTok One",
 "TikTok Store": "TikTok Store", "Tools": "Công cụ tra cứu (Tools)", "User": "Người dùng (User)", "Video": "Video", "Verification": "Xác minh (Verification)",
 "Welcome Messages": "Tin nhắn chào mừng (Welcome Messages)",
}


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower().replace("&", "and").replace("+", "plus")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


# ---- digest -----------------------------------------------------------------------------------
def make_digest(doc_id, intro_chars=1500, head_limit=40):
    x = by_id[doc_id]
    txt = open(os.path.join(CLEAN, f"{doc_id}.md"), encoding="utf-8").read()
    body = txt.split("\n", 3)[-1]
    intro = body[:intro_chars]
    heads = [h.strip() for h in re.findall(r"(?m)^#{2,4}\s+(.+)$", body)][:head_limit]
    eps = sorted(set(re.findall(r"open_api/v1\.3/[a-z0-9_/\-]+", body)))[:25]
    params = []
    if len(body) > 0:
        params = re.findall(r"(?m)^\| ([a-z_][a-z0-9_]*) (?:\*\*\(Required\)\*\*)? ?\|", body)
    params = list(dict.fromkeys(params))[:40]
    out = [f"<!-- doc_id: {doc_id} -->", f"# {x['title']}", f"> Đường dẫn: {' > '.join(x['path'])}", f"> Độ dài nguồn: {len(body)} ký tự (đã rút gọn)", "",
           "## Phần mở đầu của nguồn", intro, "", "## Các đề mục trong tài liệu", *[f"- {h}" for h in heads], "",
           "## Endpoint được nhắc tới", *[f"- /{e}" for e in eps], "", "## Một số tham số chính", ", ".join(f"`{p}`" for p in params)]
    open(os.path.join(DIGEST, f"{doc_id}.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


# ---- phân loại ---------------------------------------------------------------------------------
LOOKUP = {"1739311040498689", "1739357589575681"}  # Location IDs, Industries (xử lý bằng script)
units = []  # (section_key, out_file, title_vi, mode, [doc_ids])


def add_units(key, out_base, title_vi, docs, mode="full"):
    """Chia docs (đã sắp theo thứ tự cây) thành các unit <= MAX_CHARS."""
    chunks, cur, size = [], [], 0
    for d in docs:
        L = by_id[d]["clean_len"] if mode == "full" else min(by_id[d]["clean_len"], 3500)
        if cur and size + L > MAX_CHARS:
            chunks.append(cur); cur, size = [], 0
        cur.append(d); size += L
    if cur:
        chunks.append(cur)
    for i, ch in enumerate(chunks, 1):
        suffix = f"-p{i}" if len(chunks) > 1 else ""
        t = title_vi + (f" — phần {i}/{len(chunks)}" if len(chunks) > 1 else "")
        units.append({"key": key, "out": f"{out_base}{suffix}.md", "title_vi": t, "mode": mode, "doc_ids": ch,
                      "chars": sum(by_id[d]["clean_len"] for d in ch)})


# 1) API Reference theo nhóm cấp 2
groups = {}
order = []
for x in idx:
    p = x["path"]
    if p[0] == "API Reference" and len(p) >= 3:
        g = p[1]
        if g not in groups:
            groups[g] = []; order.append(g)
        if x["n_children"] == 0 or x["depth"] >= 2:
            groups[g].append(x["doc_id"])
for n, g in enumerate(order, 1):
    docs = groups[g]
    mode = "digest" if g.startswith("(To be deprecated)") or g.startswith("(Deprecated)") else "full"
    # nhóm có tài liệu mô tả nhóm (depth 1) -> đặt đầu: đã không thêm vì n_children>0; thêm riêng tài liệu nhóm nếu ngắn
    gid = next(x["doc_id"] for x in idx if x["path"] == ["API Reference", g])
    if by_id[gid]["clean_len"] < 6000:
        docs = [gid] + docs
    add_units(f"apiref:{g}", f"docs/api-reference/{n:02d}-{slugify(g)}", VI.get(g, g), docs, mode)

# 2) Các phần hướng dẫn
sections = {}
sec_order = []
for x in idx:
    p = x["path"]
    if p[0] == "API Reference" or p[0] == "Appendix" or p[0] == "What's New":
        continue
    if p[0] == "Use Cases":
        key = ("Use Cases", p[1] if len(p) > 1 else "")
    elif p[0] == "Marketing API":
        key = ("Marketing API", p[1] if len(p) > 1 else "")
    elif p[0] == "Organic API":
        key = ("Organic API", p[1] if len(p) > 1 and p[1] not in ("Overview",) else "")
    else:
        key = (p[0],)
    if key not in sections:
        sections[key] = []; sec_order.append(key)
    sections[key].append(x["doc_id"])

SEC_VI = {
 ("About the Guide",): ("tong-quan/gioi-thieu-bo-tai-lieu", "Giới thiệu bộ tài liệu"),
 ("Overview",): ("tong-quan/tong-quan-va-phien-ban", "Tổng quan, phiên bản và thay đổi v1.3"),
 ("Get Started",): ("tong-quan/bat-dau", "Bắt đầu: khái niệm, quy trình, rate limit, sandbox"),
 ("FAQs",): ("tong-quan/faq", "Câu hỏi thường gặp (FAQs)"),
 ("API Playground",): ("tong-quan/api-playground", "API Playground"),
 ("API Service Status Page",): ("tong-quan/trang-thai-dich-vu", "Trang trạng thái dịch vụ API"),
 ("SDK",): ("tong-quan/sdk", "SDK"),
 ("Marketing API", ""): ("huong-dan/marketing-api-gioi-thieu", "Marketing API — giới thiệu"),
 ("Marketing API", "Overview"): ("huong-dan/marketing-api-tong-quan", "Marketing API — tổng quan"),
 ("Marketing API", "Get started"): ("huong-dan/marketing-api-xac-thuc-uy-quyen", "Marketing API — bắt đầu, xác thực và ủy quyền"),
 ("Marketing API", "Business Center"): ("huong-dan/business-center", "Hướng dẫn Business Center"),
 ("Marketing API", "Reporting"): ("huong-dan/bao-cao", "Hướng dẫn Báo cáo (Reporting)"),
 ("Marketing API", "Audience Management"): ("huong-dan/audience", "Hướng dẫn quản lý Audience"),
 ("Marketing API", "Catalog Management"): ("huong-dan/catalog", "Hướng dẫn quản lý Catalog"),
 ("Marketing API", "Creatives"): ("huong-dan/creatives", "Hướng dẫn Creatives"),
 ("Marketing API", "Campaign Management"): ("huong-dan/quan-ly-chien-dich", "Hướng dẫn quản lý chiến dịch"),
 ("Marketing API", "Ad Measurement"): ("huong-dan/do-luong-quang-cao", "Hướng dẫn đo lường quảng cáo (Ad Measurement)"),
 ("Marketing API", "TikTok Store"): ("huong-dan/tiktok-store", "Hướng dẫn TikTok Store"),
 ("Use Cases", ""): ("huong-dan/use-cases", "Use cases — tổng quan, Audience, Báo cáo"),
 ("Use Cases", "Audience integration"): ("huong-dan/use-case-audience", "Use case: tích hợp Audience"),
 ("Use Cases", "Campaign creation"): ("huong-dan/use-case-tao-chien-dich", "Use case: tạo chiến dịch (tóm tắt)"),
 ("Use Cases", "Lead generation"): ("huong-dan/use-case-lead-generation", "Use case: Lead generation"),
 ("Use Cases", "Reporting"): ("huong-dan/use-case-bao-cao", "Use case: Báo cáo"),
 ("Use Cases", "Webhook subscription"): ("huong-dan/use-case-webhook", "Use case: đăng ký Webhook"),
 ("Use Cases", "Media Mix Modeling data request"): ("huong-dan/use-case-mmm", "Use case: yêu cầu dữ liệu Media Mix Modeling"),
 ("Organic API", ""): ("organic-api/tong-quan", "Organic API — tổng quan"),
 ("Organic API", "Accounts API"): ("organic-api/accounts-api", "Organic API — Accounts API"),
 ("Organic API", "Mentions API"): ("organic-api/mentions-api", "Organic API — Mentions API"),
 ("Organic API", "TikTok One API"): ("organic-api/tiktok-one-api", "Organic API — TikTok One API"),
 ("Organic API", "Discovery API"): ("organic-api/discovery-api", "Organic API — Discovery API"),
 ("Organic API", "Spark Ads Recommendation API"): ("organic-api/spark-ads-recommendation-api", "Organic API — Spark Ads Recommendation API"),
 ("Business Messaging API",): ("business-messaging-api/business-messaging-api", "Business Messaging API"),
 ("TikTok for Business MCP Server",): ("mcp/mcp-server", "TikTok for Business MCP Server"),
 ("Skill and MCP management",): ("mcp/skill-va-mcp", "Quản lý Skill và MCP"),
}
FULL_ALL = {("Marketing API", "Reporting"), ("Use Cases", "Webhook subscription")}  # luôn dịch đầy đủ
LOW_THRESHOLD = {("Marketing API", "Ad Measurement"), ("Marketing API", "Campaign Management")}

for key in sec_order:
    docs = sections[key]
    out_base, title = SEC_VI[key]
    skey = "guide:" + "/".join(key)
    if key == ("Use Cases", "Campaign creation"):
        add_units(skey, f"docs/{out_base}", title, docs, "digest"); continue
    if key[0] in ("TikTok for Business MCP Server", "Skill and MCP management"):
        big = [d for d in docs if by_id[d]["clean_len"] > 15_000 or "connect" in " ".join(by_id[d]["path"]).lower()]
        small = [d for d in docs if d not in big]
        if small: add_units(skey, f"docs/{out_base}", title, small, "full")
        if big: add_units(skey + ":digest", f"docs/{out_base}-tom-tat", title + " (tóm tắt)", big, "digest")
        continue
    if key in FULL_ALL:
        add_units(skey, f"docs/{out_base}", title, docs, "full"); continue
    thr = 12_000 if key in LOW_THRESHOLD else DIGEST_THRESHOLD
    full_docs = [d for d in docs if by_id[d]["clean_len"] <= thr]
    dig_docs = [d for d in docs if by_id[d]["clean_len"] > thr]
    if full_docs:
        add_units(skey, f"docs/{out_base}", title, full_docs, "full")
    if dig_docs:
        add_units(skey + ":digest", f"docs/{out_base}-tom-tat", title + " (tóm tắt các tài liệu dài)", dig_docs, "digest")

# 3) Phụ lục
app = [x["doc_id"] for x in idx if x["path"][0] == "Appendix"]
app_full = [d for d in app if d not in LOOKUP and by_id[d]["clean_len"] < 80_000]
add_units("appendix", "docs/phu-luc/phu-luc", "Phụ lục: mã lỗi, enum, quyền, múi giờ…", app_full, "full")

# What's New: bản rút gọn = phần đầu (mới nhất)
whats_new_id = next((x["doc_id"] for x in idx if x["path"] == ["What's New"]), None)
if whats_new_id:
    x = by_id[whats_new_id]
    txt = open(os.path.join(CLEAN, f"{whats_new_id}.md"), encoding="utf-8").read()
    open(os.path.join(DIGEST, f"{whats_new_id}.md"), "w", encoding="utf-8").write(txt[:45_000] + "\n\n[... đã cắt bớt các mục cũ hơn ...]\n")
    units.append({"key": "whatsnew", "out": "docs/tong-quan/co-gi-moi.md", "title_vi": "Có gì mới (What's New) — các thay đổi gần đây", "mode": "digest-text", "doc_ids": [whats_new_id], "chars": 45_000})

# digest files
for u in units:
    if u["mode"] == "digest":
        for d in u["doc_ids"]:
            make_digest(d)

for i, u in enumerate(units, 1):
    u["unit_id"] = f"u{i:02d}"
    json.dump(u, open(os.path.join(UNITS, f"{u['unit_id']}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(units, open(os.path.join(ROOT, "_work", "units.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# gom thành batch cho subagent
BATCH_MAX = 175_000
def weight(u):
    return u["chars"] if u["mode"] == "full" else 4000 * len(u["doc_ids"]) + 1000
batches, cur, w = [], [], 0
for u in units:
    uw = weight(u)
    if cur and w + uw > BATCH_MAX:
        batches.append(cur); cur, w = [], 0
    cur.append(u["unit_id"]); w += uw
if cur: batches.append(cur)
os.makedirs(os.path.join(ROOT, "_work", "batches"), exist_ok=True)
for f in os.listdir(os.path.join(ROOT, "_work", "batches")): os.remove(os.path.join(ROOT, "_work", "batches", f))
uid = {u["unit_id"]: u for u in units}
for i, b in enumerate(batches, 1):
    json.dump({"batch_id": f"b{i:02d}", "units": [uid[x] for x in b]}, open(os.path.join(ROOT, "_work", "batches", f"b{i:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("batches:", len(batches))
covered = {d for u in units for d in u["doc_ids"]}
print("units:", len(units), "| docs covered:", len(covered), "/", len(idx))
tot_full = sum(u["chars"] for u in units if u["mode"] == "full")
print("full chars:", tot_full)
outs = [u["out"] for u in units]
assert len(outs) == len(set(outs)), "trùng tên file"
for u in units:
    print(u["unit_id"], u["mode"][:6], f"{u['chars']:7d}", len(u["doc_ids"]), u["out"])
