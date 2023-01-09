"""
List Ops
"""


def append(list1, list2):
    """
    `append` (*given two lists, add all items in the second list to the end of the first list*);
    """
    return list1 + list2


def concat(lists):
    """
    `concatenate` (*given a series of lists, combine all items in all lists
        into one flattened list*);
    """
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    """
    `filter` (*given a predicate and a list, return the list of all items for
        which `predicate(item)` is True*);
    """
    return [item for item in list if function(item)]


def length(list):
    """
    `length` (*given a list, return the total number of items within it*);
    """
    return len(list)


def map(function, list):
    """
    `map` (*given a function and a list, return the list of the results of
        applying `function(item)` on all items*);
    """
    return [function(item) for item in list]


def foldl(function, list, initial):
    """
    `foldl` (*given a function, a list, and initial accumulator, fold (reduce)
        each item into the accumulator from the left using `function(accumulator, item)`*);
    """
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    """
    `foldr` (*given a function, a list, and an initial accumulator, fold (reduce)
        each item into the accumulator from the right using `function(item, accumulator)`*);
    """
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    """
    `reverse` (*given a list, return a list with all the original items, but in reversed order*);
    """
    return list[::-1]
