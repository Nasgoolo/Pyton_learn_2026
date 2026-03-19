def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if text1 == text2:
        return False

    return sorted(text1) == sorted(text2)