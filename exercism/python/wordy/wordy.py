"""
wordy.py
"""

import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_(node):
    """
    eval for arithmeticsas in simpleeval
    """
    # <number>
    if isinstance(node, ast.Num):
        return node.n
    # <left> <operator> <right>
    if isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    # <operator> <operand> e.g., -1
    if isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    raise TypeError(node)


def unk_op(question):
    """
    simple generator to check if the operation is known
    """
    for value in question:
        yield value.isalpha() and value not in ("What", "is")


def answer(question):
    """
    Parse and evaluate simple math word problems returning the answer as an integer.
    """

    if not question.startswith('What is'):
        raise ValueError("unknown operation")

    question = question.replace("What is ", "").replace("?", "").replace("?", "")
    question = question.replace("plus", "+").replace("multiplied by", "*").replace("minus", "-")
    question = question.replace("divided by", "/").split()

    # this should be replaced with a loop
    question.insert(0, "(")
    question.insert(4, ")")

    if any(list(unk_op(question))):
        raise ValueError("unknown operation")

    try:
        return eval_(ast.parse(" ".join(question), mode='eval').body)
    except Exception as exception:
        raise ValueError("syntax error") from exception
