def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    Len = len(plaintext)
    while len(keyword) != Len:
        a = Len - len(keyword)
        if a >= len(keyword):
            keyword *= 2
        else:
            keyword += keyword[:a]
    keyword = keyword.upper()
    for i in range(len(plaintext)):
        shift = ord(keyword[i]) - 65
        p = ord(plaintext[i])
        p += shift
        if p > 122:
            p -= 26
        elif p > 90:
            p -= 26
        ciphertext += chr(p)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    Len = len(ciphertext)
    while len(keyword) != Len:
        a = Len - len(keyword)
        if a >= len(keyword):
            keyword *= 2
        else:
            keyword += keyword[:a]
    keyword = keyword.upper()
    for i in range(len(ciphertext)):
        shift = ord(keyword[i]) - 65
        p = ord(ciphertext[i])
        p -= shift
        if p < 65:
            p += 26
        if p > 90 and p < 97:
            p += 26
        plaintext += chr(p)
    return plaintext

ex1 = encrypt_vigenere("ATTACKATDAWN", "LEMON")
ex2 = decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
print(ex1, ex2)
