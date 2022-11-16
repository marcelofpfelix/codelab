"""
roman numerals
"""
import math


symbol1 = ["I", "X", "C", "M"]
symbol5 = ["V", "L", "D"]


def get_digit(number, index):
    """
    get a digit from a number
    """
    return number // 10**index % 10


def roman(number):
    """
    convert Hindu–Arabic numeral system to roman

    this version aims to be versatile, simply by adding
    the ordered simbols to the list
    while substracting values from
    ['M','CM',D','CD','C','XC','L','XL','X','IX','V','IV', 'I']
    would also be a good alternative
    """
    romano = ""

    # get the number of digits
    lenght = int(math.log10(number))+1

    for index in range(lenght):
        digit = get_digit(number, index)
        letter = ""

        # 4 or 9
        if digit % 5 == 4:
            if digit % 5 == 4:
                letter += symbol1[index]
            if digit > 5:
                letter += symbol1[index + 1]
            else:
                letter += symbol5[index]
        else:
            # adds symbol5
            if digit > 4:
                letter += symbol5[index]
                digit = digit - 5
            # and then the remain symbol1
            for _ in range(digit):
                letter += symbol1[index]
        romano = letter + romano

    return romano
