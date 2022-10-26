"""
Sum of Multiples
"""


def sum_of_multiples(limit, multiples):
    """
    sum of all the unique multiples of particular numbers up to
    but not including that number

        arg limit: (int) limit number
        arg multiples: (list) list of factors
        return: (int) sum of multiples
    """

    # # simple
    # sum = 0
    # for index in range(limit):
    #   for number in multiples:
    #     if number:
    #         if index % number == 0:
    #             sum+=index
    #             break
    # return sum

    # # improve efficiency, using a set,
    # # range increment and sum.
    # values = set()
    # for number in multiples:
    #     if number:
    #         for index in range(number,limit,number):
    #                 values.add(index)
    # return sum(values)

    # the same but using set comprehension
    return sum({index for number in multiples if number
                for index in range(number, limit, number)})
