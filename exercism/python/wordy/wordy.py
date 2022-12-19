"""
wordy.py
"""

#from ast import literal_eval


def answer(question):
    """
    Parse and evaluate simple math word problems returning the answer as an integer.
    """

    if not question.startswith('What is'):
        raise ValueError("unknown operation")

    question = question.replace("What is ","").replace("?","").replace("?","").replace("plus", "+").replace("multiplied by","*").replace("minus", "-").replace("divided by", "/").split()

    # this should be replaced with a loop
    question.insert(0, "(")
    question.insert(4, ")")

    if any([x.isalpha() for x in question if x not in ("What", "is")]):
        raise ValueError("unknown operation")

    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")
