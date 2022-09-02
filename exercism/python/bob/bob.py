"""
Bob
"""

import re


def response(hey_bob):
    """
    Bob is a lackadaisical teenager. In conversation,
    his responses are very limited.

        arg hey_bob: (string) phrase from Bob's conversational partner.
    """
    # question
    if hey_bob.strip().endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    # empty
    if not re.search('[a-zA-Z0-9]', hey_bob):
        return 'Fine. Be that way!'

    return "Whatever."
