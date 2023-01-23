"""
atbash-cipher
"""

from string import ascii_lowercase


def encode(plain_text):
    """
    encodes, using the Atbash cipher
    """
    plain_text = _cypher(_clean(plain_text))
    # adds the space per chunk
    return ' '.join(plain_text[i:i+5] for i in range(0, len(plain_text), 5))


def decode(ciphered_text):
    """
    decodes, using the Atbash cipher
    """
    return _clean(_cypher(ciphered_text))


def _cypher(text):
    """
    private function
    could also be done with text_list[index]= chr(122-ord(char)+97)
    """
    return text.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))


def _clean(text):
    """
    private function
    remove non-alpha chars
    could also be done with plain_text = re.sub(r'[W_]+', '', plain_text)
    """
    return "".join([c.lower() for c in text if c.isalnum()])
