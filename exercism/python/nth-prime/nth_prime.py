"""
This module contains a function that returns the nth prime number.
"""


def prime(number):
    """
    Returns the nth prime number.
    :param number: the nth prime number to return
    :return: the nth prime number
    """

    if number == 0:
        raise ValueError("there is no zeroth prime")
    # add the first prime to the list
    primes = [2]
    index = 3
    while len(primes) < number:
        # checks whether n is divisible by any of the prime 
        if all(index % prime > 0 for prime in primes):
            primes.append(index)
        # all prime numbers greater than 2 are odd
        index += 2
    # return the last prime in the list
    return primes[-1]