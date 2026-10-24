import re

txt = open("tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md").read()

# Test count of remaining untranslated words before
parts = txt.split("```")
prose_before = "\n".join([parts[k] for k in range(0, len(parts), 2)])
en_words_before = re.findall(r"\b[A-Za-z]{4,}\b", prose_before)
allowed = {
    "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
    "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
    "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
}
untrans_before = [w for w in en_words_before if w.lower() not in allowed]
print(f"Untranslated words before: {len(untrans_before)}")
