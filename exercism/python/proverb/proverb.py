"""
proverb
"""


def proverb(*inputs, qualifier=None):
    """
    Given a list of inputs, generate the relevant proverb
    """

    if not inputs:
        return []

    data = [f"For want of a {inputs[index]} the {inputs[index +1]} was lost."
            for index, _ in enumerate(inputs[:-1])]

    data.append(f"And all for the want of a {qualifier + ' ' if qualifier else ''}{inputs[0]}.")

    return data
