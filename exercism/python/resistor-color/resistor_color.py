"""
Resistor Color
"""


def color_code(color):
    """
    gets the resistence color code index

    Parameters:
        color (string): the resistence color

    Returns:
        (int): the color code index
    """
    return colors().index(color)


def colors():
    """
    Get a list of resistence colors

    Returns:
        (list): the ordered list of colors
    """
    return ["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
            ]
