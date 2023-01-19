"""
Acronym
"""

import re


def abbreviate(words):
    """
    simple acronym:
    a = words[0]
    words = words.replace("_", "").replace("- ", "")

    for index, char in enumerate(words):
        if char == ' ' or char == '-':
            a = a + words[index + 1]
    return a.upper()
    """

    # smart: get the words
    return ''.join(word[0].upper() for word in re.findall(r"[a-zA-Z']+", words))
