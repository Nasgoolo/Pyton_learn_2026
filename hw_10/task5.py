import re


def normalize_text(text):
    parts = re.split(r'([!?.])', text)
    normalized_parts = map(lambda s: s.strip().capitalize() if s not in "!?." else s, parts)
    result = "".join(normalized_parts).replace("!", "! ").replace("?", "? ").replace(".", ". ")
    return result.strip()

print(normalize_text("THIS IS some Text. And this text, is just an EXAMPLE! trust me"))
