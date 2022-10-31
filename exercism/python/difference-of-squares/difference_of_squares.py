
"""
Difference of Squares
"""


def square_of_sum(number):
    """
    square of the sum

    using the partial sum:
        $sum_(n=1)^k n = 1/2 k (k + 1)$
    https://www.wolframalpha.com/input?i=sum+n%2C+n%3D1+to+infinity
    """
    return (number*(number+1)//2)**2

    # # using generator expression
    # return sum(index for index in range(number+1))**2
    # # or simply
    # return sum(range(number+1))**2


def sum_of_squares(number):
    """
     sum and the sum of the squares

    using the partial sum:
        $sum_(n=1)^k n^2 = 1/6 k (k + 1) (2 k + 1)$
    https://www.wolframalpha.com/input?i=sum+n%5E2%2C+n%3D1+to+infinity
    """

    return number*(number+1)*(2*number+1)//6

    # # using generator expression
    # return sum(index**2 for index in range(number+1))


def difference_of_squares(number):
    """
    The difference between the square of the sum and the sum of the squares
    """

    # # simple solution:
    # sums = 0
    # squares = 0
    # for index in range(number+1):
    #     sums += index
    #     squares += index**2
    # return sums**2 - squares

    return square_of_sum(number) - sum_of_squares(number)
