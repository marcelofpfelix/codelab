"""
leap
"""


def leap_year(year):
    """
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400

    Args:
        year (int)

    Returns:
        (bool)
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
