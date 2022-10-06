"""
Gigasecond
"""

from datetime import timedelta


def add(moment):
    """
    Given a moment, determine the moment that would be after a gigasecond
    has passed.
    agr

        arg moment: (datetime) a moment.
        return: (datetime) the moment after a gigasecond
    """
    return moment + timedelta(0, 10**9)
