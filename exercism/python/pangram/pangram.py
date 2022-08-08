""" pangram exercise """

from string import ascii_lowercase


def is_pangram(sentence):
    """
    Determine if a sentence is a pangram.

    Returns:
        (bool): true if it's a pangram
    """
    alphabet = set(ascii_lowercase)

    return alphabet.issubset(sentence.lower())
