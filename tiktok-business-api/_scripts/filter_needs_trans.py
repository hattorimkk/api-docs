import re

lines = open("tiktok-business-api/_work/u101_unique_en_lines.txt").read().splitlines()

# Patterns that are considered already translated or pure enum/code
def needs_translation(text):
    # remove count prefix
    parts = text.split("\t", 1)
    if len(parts) == 2:
        line = parts[1]
    else:
        line = parts[0]
    
    # Check if purely markdown table divider or symbols
    if re.match(r"^[\s\|\-\:\`\d\.\,\(\)\/]+$", line):
        return False
        
    # Check if there are English words (at least 3 characters) not inside backticks and not standard keywords
    # Remove code blocks and inline code
    clean_line = re.sub(r"`[^`]+`", "", line)
    # Remove markdown links target
    clean_line = re.sub(r"\]\([^\)]+\)", "]", clean_line)
    
    # Common allowed tech words
    allowed = {
        "tiktok", "api", "curl", "url", "id", "ids", "json", "http", "https", "post", "get",
        "app", "web", "android", "ios", "pixel", "gmv", "max", "cbo", "ocpm", "cpc", "cpa",
        "roas", "smart", "spark", "ads", "lead", "traffic", "vbo", "iap", "cta", "catalog",
        "carousel", "video", "feed", "csv", "pangle", "lemon8", "pinedrama", "doubleverify", "ias", "zefr",
        "status", "mode", "type", "true", "false", "null", "bc", "o2o", "mini", "series", "games", "dramas",
        "streaming", "travel", "e-commerce", "showcase", "store", "live", "sku", "deeplink", "utm", "html"
    }
    
    words = re.findall(r"\b[A-Za-z]{3,}\b", clean_line)
    untranslated = [w for w in words if w.lower() not in allowed]
    return len(untranslated) >= 1

to_translate = [l for l in lines if needs_translation(l)]
print(f"Lines truly needing translation: {len(to_translate)} / {len(lines)}")
with open("tiktok-business-api/_work/u101_to_translate.txt", "w", encoding="utf-8") as f:
    for l in to_translate:
        f.write(l + "\n")
