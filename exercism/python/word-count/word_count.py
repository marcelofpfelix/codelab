"""
word-count
"""

import re
from collections import Counter


def count_words(sentence):
    """
    simple:
    sentence = sentence.lower().replace(',', ' ').replace('_', ' ').split()

    dict = {}
    for _, word in enumerate(sentence):
        word = word.strip('?!,\'\".:;/~$()-@#%^&')
        dict[word] = 1 + dict.setdefault(word, 0)
    return dict

    or {word: words.count(word) for word in words}
    """

    # count the number words defined by a regex
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))
