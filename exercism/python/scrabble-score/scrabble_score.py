"""
Scrabble Score
"""

POINT_MAP = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10,
}


def score(word):
    """
    Given a word, compute the Scrabble score for that word.

    simple solution:
    score = 0
    for c in word.lower():
        for x, y in thisdict.items():
            if c in x and c.isalpha():
              score+=y
              break
    return score
    """

    # char dict for easier calculation
    points = {char: point for chars, point in POINT_MAP.items() for char in chars}

    return sum(points[char] for char in word.lower())
