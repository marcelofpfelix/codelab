"""
Hamming
"""


def distance(strand_a, strand_b):
    """
    Calculate the Hamming Distance between two DNA strands.

        arg strand_a: (str) strand of DNA
        arg strand_b: (str) strand of DNA
        return: the Hamming Distance between two DNA strands
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))
