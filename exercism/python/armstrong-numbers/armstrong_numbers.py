"""
Armstrong Numbers
"""


def is_armstrong_number(number):
    """
    determine whether a number is an Armstrong number.

    :param number: (int) a number to test
    :return: (bool) if is an Armstrong number
    """
    string = str(number)
    strlen = len(string)
    total = 0

    for char in string:
        total = total + int(char)**strlen

    return number == total

    # simplified alternative
    # return number == sum(int(char)**strlen for char in string)
