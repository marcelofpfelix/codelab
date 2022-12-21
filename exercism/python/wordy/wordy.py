"""
wordy.py
"""

import re


def answer(question):
    """
    Parse and evaluate simple math word problems returning the answer as an integer.
    """

    # validate syntax
    if not question.startswith('What is'):
        raise ValueError("unknown operation")

    op_regex = re.compile(r'(plus|minus|divided|multiplied)')
    num_regex = re.compile(r'-?\d+')

    operations = list(re.findall(op_regex, question))
    numbers = list(re.findall(num_regex, question))

    # returns error if numbers and operators mismatch
    if len(operations) != (len(numbers) - 1):
        raise ValueError("syntax error")

    if (not re.match(r"What is \d\?", question)) and len(numbers) == 1:
        raise ValueError("unknown operation")

    if not re.match(r"What is -?\d+(?: (?:plus|minus|divided by|multiplied by) -?\d+)*\?",
                    question):
        raise ValueError("syntax error")

    total = int(numbers[0])

    for index, operation in enumerate(operations):
        number = int(numbers[index+1])
        if operation == "plus":
            total += number
        elif operation == "minus":
            total -= number
        elif operation == "divided":
            total /= number
        elif operation == "multiplied":
            total *= number

    return total
