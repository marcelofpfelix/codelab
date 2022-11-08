"""
Luhn
"""


class Luhn:
    """
    Luhn algorithm
    """

    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        """
        Given a number determine whether or not it is valid per the Luhn formula.
        index manipulation would be more complex:
        card = [int(value) for value in self.card_num]
        card[-2::-2] = [2*value - 9*(value>4) for value in card[-2::-2]]
        """

        total = 0
        index = 1

        parity = len(self.card_num) % 2
        for index, value in enumerate(self.card_num, start=1):
            if value.isdigit():
                if index % 2 == parity:
                    total += int(value)
                elif int(value) > 4:
                    total += 2*int(value) - 9
                else:
                    total += 2*int(value)
            else:
                return False

        return total % 10 == 0 and index > 1
