import re

txt = open("tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md").read()
matches = list(re.finditer(r"<a id=\"doc-(\d+)\"></a>", txt))

for i, m in enumerate(matches):
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(txt)
    doc_id = m.group(1)
    doc_chunk = txt[start:end]
    
    # check english words in doc_chunk prose
    parts = doc_chunk.split("```")
    prose = "\n".join([parts[k] for k in range(0, len(parts), 2)])
    
    en_words = re.findall(r"\b[A-Za-z]{4,}\b", prose)
    allowed = {
        "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
        "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
        "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
    }
    untrans = [w for w in en_words if w.lower() not in allowed]
    print(f"Doc {i+1:2d} ({doc_id}): {len(untrans):4d} untranslated word occurrences")
