"""
ISBN Verifier
"""


def is_valid(isbn):
    """
    ISBN-10 verification process

    using a replace a re.match and
        digits = [value == 'X' and 10 or int(value) for value in isbn]
        summ = sum(value * (10 -  index) for index, value in enumerate(digits))
    doesn't seem as efficient
    """
    total = 0
    multi = 10

    for value in isbn:
        if value.isdigit():
            total = total + int(value) * multi
            multi -= 1
        elif value == '-':
            continue
        elif value == 'X' and multi == 1:
            total = total + 10 * multi
            multi -= 1
        else:
            return False

    return total % 11 == 0 and not multi
