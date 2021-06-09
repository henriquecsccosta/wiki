from wiki import ExtractKeysFromWiki

kws = ExtractKeysFromWiki("Coronavirus")
for kw in kws:
    print(kw[0])