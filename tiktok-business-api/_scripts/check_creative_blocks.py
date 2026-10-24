import re, glob, os

files = [
  'docs/api-reference/35-creative-pre-review.md',
  'docs/api-reference/36-creative-portfolios.md',
  'docs/api-reference/37-creative-reports.md',
  'docs/api-reference/38-creative-tools.md',
  'docs/api-reference/47-images.md',
  'docs/api-reference/52-music.md',
  'docs/api-reference/56-playable-ads.md',
  'docs/api-reference/60-smart-creative.md',
  'docs/api-reference/71-video.md',
  'docs/huong-dan/creatives.md'
]

base_dir = '/Users/hattorimk/Desktop/api-docs/tiktok-business-api'
for f in files:
    path = os.path.join(base_dir, f)
    text = open(path).read()
    py_cnt = len(re.findall(r'```python', text))
    curl_cnt = len(re.findall(r'curl', text))
    print(f"{f:45s}: py={py_cnt}, curl={curl_cnt}, len={len(text)}")
