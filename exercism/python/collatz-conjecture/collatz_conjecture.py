"""
Collatz Conjecture
"""


def steps(number):
    """
    Take any positive integer n. If n is even, divide n by 2
    to get n / 2. If n is odd, multiply n by 3 and add 1 to
    get 3n + 1. Repeat the process indefinitely.

    return the number of steps required to reach 1.
    """

    count = 0

    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    while number != 1:
        count += 1
        # Conditional expression
        number = 3 * number + 1 if number % 2 else number / 2

    return count
