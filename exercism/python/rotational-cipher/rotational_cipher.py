"""
otational-cipher
"""


def cipher(char, key):
    """
    sums the key using % 26
    """
    lower = ord("a")
    upper = ord("A")
    start = upper

    if ord(char) >= lower:
        start = lower
    if ord(char) >= upper:
        return chr((ord(char) + key - start) % 26 + start)

    return char


def rotate(text, key):
    """
    a simple shift cipher that relies on transposing all the letters in the alphabet
    using an integer key between `0` and `26`

    an elegant solution would be:
    rot = ascii_lowercase[key:] + ascii_lowercase[:key]
    return chars.translate(str.maketrans(ascii_lowercase +
           ascii_lowercase.upper(), rot + rot.upper()))
    """
    text_list = list(text)

    for index, char in enumerate(text_list):
        text_list[index] = cipher(char, key)

    return "".join(text_list)
