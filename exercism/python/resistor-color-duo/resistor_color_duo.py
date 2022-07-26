"""
Resistor Color Duo
"""



def value(colors):
    # color_list = colors.split(':')

    color_value = {
        "black":  "0",
        "brown":  "1",
        "red":    "2",
        "orange": "3",
        "yellow": "4",
        "green":  "5",
        "blue":   "6",
        "violet": "7",
        "grey":   "8",
        "white":  "9",
    }

    colors_len  = len(colors)
    print(colors_len)
    if colors_len > 1:
        return int( color_value[colors[0]] +  color_value[colors[1]])
        # alternative
        # return color_list().index(colors[0]) * 10 + color_list().index(colors[1])
    elif colors_len == 1:
        return int(color_value[colors[0]])
    else: 
        return 0


def color_list():
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