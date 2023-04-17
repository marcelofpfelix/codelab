"""
Simple Cipher
"""

from itertools import cycle
from string import ascii_lowercase
from secrets import choice


class Cipher:
    """
    Simple Cipher class
    """
    def __init__(self, key=''.join(choice(ascii_lowercase) for _ in range(100))):
        self.key = key

    def encode(self, text, shift=1):
        """
        encodes, using the simple cipher
        * 26 represents the number of letters in the alphabet
        * 97 is the ascii value for 'a'
        """
        # zip the text and key, then shift the text by the key
        return ''.join(
            chr((ord(t) - 97 + shift * (ord(k) - 97)) % 26 + 97)
            for t, k in zip(text, cycle(self.key)))

    def decode(self, text):
        """
        decodes, using the simple cipher
        """
        return self.encode(text, shift=-1)
