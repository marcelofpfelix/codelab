"""
triangle
"""


def equilateral(sides):
    """
    equal sides

    alternative:
        return triangle(sides) and sides[0] == sides[1] == sides [2]
    """
    return triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    """
    2 or more equal sides
    """

    return triangle(sides) and not scalene(sides)


def scalene(sides):
    """
    different sides

    alternative:
        return triangle(sides) and sides[0] != sides[1] != sides [2] and sides[0] != sides [2]

        a, b, c = sorted(sides)
        return 0 < a < b < c < a + b
    """
    return triangle(sides) and len(set(sides)) == 3


def triangle(sides):
    """
    alternative:
        return triangle(sides) and sides[0] != sides[1] != sides [2] and sides[0] != sides [2]

        a, b, c = sorted(sides)
        return a * b * c != 0 and a + b >= c

        return all((sides[(index)%3] + sides[(1 + index)%3] >= sides[(2 + index)%3])
        and (value > 0) for index, value in enumerate(sides))
    """
    return all(sides) and (sum(sides) >= max(sides)*2)
