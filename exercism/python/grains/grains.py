"""
Grains
"""


def square(number):
    """
    Calculate the number of grains of wheat on a chessboard given that the
    number on each square doubles.

        arg number: int square to check (which must be between 1 and 64).
        return: int grains of rice on that square.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)
    # return 1 << (number - 1) left shift by n bits is a more efficient
    # way to do a multiplication by pow(2, n)


def total():
    """
    Count the total number of grains.

        return: int total number of grains.
    """
    return 2**64 - 1
