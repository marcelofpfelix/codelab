"""
Flatten Array

Alternatives
in the case of a simple list of list
    return [val for sublist in iterable for val in sublist]

simple solution:

    def flatten(iterable):
        flat = []
        for value in iterable:
            if hasattr(value, '__iter__'):
                flat += flatten(value)
            elif value != None:
                flat.append(value)
        return flat
"""


def roller(iterable):
    """
    using a  generator function and calling
    the function recursively
    """

    for value in iterable:
        # isinstance(item, (tuple, list)):
        if hasattr(value, '__iter__'):
            # for sub_value in roller(value):
            #     yield sub_value
            yield from roller(value)
        elif value is not None:
            yield value


def flatten(iterable):
    """
    Take a nested list and return a single flattened list
    with all values except nil/null.
    """

    return list(roller(iterable))
