"""
Extract-Transform-Load
"""


def transform(legacy_data):
    """
    switching keys and values in a dictionary in python

        arg legacy_data: (dict) legacy format.
        return: (dict) new format
    """
    # first idea

    return {z.lower(): x for x, y in legacy_data.items() for z in y}

    # alternative
    # return {y.lower(): x for x in legacy_data for y in legacy_data[x]}
