This package allows users to extract keywords from wikipedia articles given an input subject

```bash
from wiki import ExtractKeysFromWiki

kws = ExtractKeysFromWiki("Coronavirus")
for kw in kws:
    print(kw[0])