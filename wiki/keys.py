import wikipedia
import yake

def ExtractKeysFromWiki(subject):
    wikipedia.set_lang("pt")
    text = wikipedia.summary(subject)

    kws = yake.KeywordExtractor(lan="pt")
    keywords = kws.extract_keywords(text)

    return keywords