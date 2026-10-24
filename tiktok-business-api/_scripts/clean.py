#!/usr/bin/env python3
"""Làm sạch docs thô (_raw/docs/*.json) thành Markdown gọn (_clean/<doc_id>.md).

- xtable -> bảng Markdown chuẩn (giữ độ sâu lồng nhau của '#', '##' bằng '↳')
- xcodeblock -> code fence
- HTML (<br>, <ul>/<li>, <b>, <span>...) -> text gọn
- Bỏ mục "Comparing v1.2 and v1.3"
- Link nội bộ (id=<doc_id>) -> [text](doc:<doc_id>) để sau này map sang file cục bộ
"""
import html, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW = os.path.join(ROOT, "_raw", "docs")
OUT = os.path.join(ROOT, "_clean")
os.makedirs(OUT, exist_ok=True)

LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://(?:ads|business-api)\.tiktok\.com/(?:marketing_api|portal)/docs\?[^)\s]*?id=(\d+)[^)\s]*)\)")
LINK2_RE = re.compile(r"\[([^\]]*)\]\((https?://business-api\.tiktok\.com/portal/docs/([a-z0-9\-]+)/v1\.3)\)")
HTMLLINK_RE = re.compile(r'<a\s+[^>]*href="[^"]*?id=(\d+)[^"]*"[^>]*>(.*?)</a>', re.S | re.I)


def inline_html(s: str) -> str:
    s = html.unescape(s)
    s = HTMLLINK_RE.sub(lambda m: f"[{m.group(2)}](doc:{m.group(1)})", s)
    s = re.sub(r'<a\s+[^>]*href="#[^"]*"[^>]*>(.*?)</a>', r"\1", s, flags=re.S | re.I)
    s = re.sub(r"<a\s+[^>]*href=\"([^\"]*)\"[^>]*>(.*?)</a>", r"[\2](\1)", s, flags=re.S | re.I)
    s = re.sub(r"</?(ul|ol)[^>]*>", "", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", " • ", s, flags=re.I)
    s = re.sub(r"</li>", "", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", " ⏎ ", s, flags=re.I)
    s = re.sub(r"</?p[^>]*>", " ⏎ ", s, flags=re.I)
    s = re.sub(r"</?(span|b|strong|i|em|u|div|font|sup|sub|code)[^>]*>", lambda m: "**" if m.group(1).lower() in ("b", "strong") else "", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"(?:\s*⏎\s*){2,}", " ⏎ ", s)
    s = re.sub(r"\s*⏎\s*", " ⏎ ", s).strip()
    s = re.sub(r"^⏎\s*|\s*⏎$", "", s)
    s = s.replace("|", "\\|") if False else s
    return s


def split_row(line: str):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    # tách theo | không bị escape và không nằm trong backtick
    cells, cur, tick = [], [], False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick and (i == 0 or line[i - 1] != "\\"):
            cells.append("".join(cur)); cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def convert_table(block: str) -> str:
    lines = [l for l in block.split("\n") if l.strip()]
    if not lines:
        return ""
    rows = []
    for l in lines:
        raw = l.strip()
        depth = 0
        m = re.match(r"^(#+)\s*\|", raw)
        if m:
            depth = len(m.group(1)); raw = raw[len(m.group(1)):]
        cells = split_row(raw)
        rows.append((depth, cells))
    # header
    hdr = rows[0][1]
    hdr = [re.sub(r"\{[^}]*%\}", "", inline_html(c)).strip() for c in hdr]
    n = len(hdr)
    out = ["| " + " | ".join(hdr) + " |", "|" + "---|" * n]
    for depth, cells in rows[1:]:
        if all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in cells if c.strip()):
            continue
        cells = [inline_html(c) for c in cells]
        if cells:
            first = cells[0]
            first = re.sub(r"\{\s*Required\s*\}", " **(Required)**", first, flags=re.I)
            first = re.sub(r"\{\s*Optional\s*\}", "", first, flags=re.I)
            first = first.strip()
            if depth > 0:
                first = "↳" * depth + " " + first
            cells[0] = first
        cells = (cells + [""] * n)[:n] if len(cells) <= n else cells[: n - 1] + [" | ".join(cells[n - 1:])]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def clean(md: str) -> str:
    md = md.replace("\r\n", "\n").replace("\r", "\n")
    # bỏ mục so sánh v1.2/v1.3
    md = re.sub(r"(?ms)^#{1,4}\s*Comparing v1\.2 and v1\.3.*?(?=^#{1,4}\s|\Z)", "", md)
    # autolink <https://...> -> `https://...`
    md = re.sub(r"<(https?://[^\s>]+)>", lambda m: "`" + m.group(1) + "`", md)
    # xtable
    md = re.sub(r"```xtable\n(.*?)\n```", lambda m: "\n" + convert_table(m.group(1)) + "\n", md, flags=re.S)
    # xcodeblock: (code Name lang)  ... (/code);
    def code(m):
        body = m.group(1)
        parts = re.split(r"\(code\s+([^\s)]+)\s*([^)]*)\)\n?", body)
        out = []
        # parts: [pre, name, lang, content, name, lang, content...]
        i = 1
        while i < len(parts):
            name, lang, content = parts[i], parts[i + 1].strip(), parts[i + 2]
            content = re.sub(r"\(/code\);?\s*$", "", content.strip("\n")).rstrip()
            out.append(f"```{lang}\n// {name}\n{content}\n```")
            i += 3
        return "\n".join(out)
    md = re.sub(r"```xcodeblock\n(.*?)\n```", code, md, flags=re.S)
    # callout quote HTML
    md = re.sub(r'<span style="[^"]*">\s*\*\*(Note|Important|Warning|Tip)\*\*\s*</span>(<br>)?', lambda m: f"**{m.group(1)}:** ", md, flags=re.I)
    # links
    md = LINK_RE.sub(lambda m: f"[{m.group(1)}](doc:{m.group(3)})", md)
    md = LINK2_RE.sub(lambda m: f"[{m.group(1)}](slug:{m.group(3)})", md)
    # html ngoài bảng/code: xử lý theo dòng, tránh động vào code fence
    out, in_code = [], False
    for line in md.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line); continue
        if in_code or line.startswith("|"):
            out.append(line); continue
        if "<" in line or "&" in line:
            line = inline_html(line).replace(" ⏎ ", "  \n") if False else re.sub(r" ⏎ ", " ", inline_html(line))
        out.append(line)
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


def main():
    idx = json.load(open(os.path.join(ROOT, "_raw", "index.json"), encoding="utf-8"))
    tot = 0
    for x in idx:
        d = json.load(open(os.path.join(RAW, f"{x['doc_id']}.json"), encoding="utf-8"))
        body = clean(d.get("content_data") or "")
        head = [f"<!-- doc_id: {x['doc_id']} -->", f"# {x['title']}", f"> Đường dẫn: {' > '.join(x['path'])}", ""]
        txt = "\n".join(head) + body
        open(os.path.join(OUT, f"{x['doc_id']}.md"), "w", encoding="utf-8").write(txt)
        x["clean_len"] = len(txt)
        tot += len(txt)
    json.dump(idx, open(os.path.join(ROOT, "_raw", "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("clean total chars:", tot)


if __name__ == "__main__":
    main()
