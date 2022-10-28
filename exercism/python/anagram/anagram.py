"""
anagram.py
"""


def find_anagrams(word, candidates):
    """
    Given a target word and a set of candidate words, this exercise requests
    the anagram set: the subset of the candidates that are anagrams of the
    target.

        arg word: (int) word to check
        arg candidates: (set) list of candidates
        return: (set) of anagrams
    """

    values = set()
    word = word.casefold()
    word_test = sorted(word.casefold())

    for candidate in candidates:
        test_candidate = candidate.casefold()
        if word_test == sorted(test_candidate) and word != test_candidate:
            values.add(candidate)

    return values
