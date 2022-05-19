import unicodedata

def remove_special_characters(encodedStr):
    return unicodedata.normalize('NFKD', encodedStr).encode('ascii', 'ignore').decode()

def equal_ignore_cases(strToCompare, strToMatch):
    return isinstance(strToCompare, str) and remove_special_characters(strToCompare).lower() == strToMatch