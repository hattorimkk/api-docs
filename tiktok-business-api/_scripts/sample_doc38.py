txt = open("tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md").read()
idx = txt.find("doc-1853377390815233")
doc38 = txt[idx:idx+4000]
print(doc38[:3000])
