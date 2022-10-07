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
    k = ""
    if plaintext == plaintext.lower():
        plaintext = plaintext.upper()
        k = 1
    elif plaintext == plaintext.capitalize():
        plaintext = plaintext.upper()
        k = 0
    for i in range(len(plaintext)):
        shift = ord(keyword[i]) - 65
        p = ord(plaintext[i])
        if p >=65 and p < 91:
            p += shift
            if p > 90:
                p -= 26
        elif p >= 91:
            p += shift
        ciphertext += chr(p)
    if k:
        ciphertext = ciphertext.lower()
    elif k == 0:
        ciphertext = ciphertext.capitalize()
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
    k = ""
    if ciphertext == ciphertext.lower():
        ciphertext = ciphertext.upper()
        k = 1
    elif ciphertext == ciphertext.capitalize():
        ciphertext = ciphertext.upper()
        k = 0
    for i in range(len(ciphertext)):
        shift = ord(keyword[i]) - 65
        p = ord(ciphertext[i])
        if p >= 65 and p < 91:
            p -= shift
            if p < 65:
                p += 26
        elif p > 90:
            p -= shift
        plaintext += chr(p)
    if k:
        plaintext = plaintext.lower()
    elif k == 0:
        plaintext = plaintext.capitalize()
    return plaintext

ex1 = encrypt_vigenere("python", "a")
ex2 = decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
print(ex1, ex2)
