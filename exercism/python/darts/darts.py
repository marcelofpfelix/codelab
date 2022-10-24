"""
Darts
"""


def score(coord_x, coord_y):
    """
    Returns the earned points in a single toss of a Darts game.
    agr

        arg coord_x: (int) cordinate.
        arg coord_y: (int) cordinate.
        return: (int) points
    """
    throw = (coord_x**2) + (coord_y**2)
    if throw > 100:
        return 0
    if throw > 25:
        return 1
    if throw > 1:
        return 5
    return 10

    # radius is a power of 2, to simplify.
