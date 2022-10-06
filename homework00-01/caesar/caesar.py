from asyncio.proactor_events import _ProactorDuplexPipeTransport
from pydoc import plain


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    a = ""
    k = ""
    if plaintext == plaintext.lower():
        plaintext = plaintext.upper()
        k = 1
    elif plaintext == plaintext.capitalize():
        plaintext = plaintext.upper()
        k = 0
    for i in range(len(plaintext)):
        a = ord(plaintext[i])
        if a >= 65 and a < 91:
            a += shift
            if a > 90:
                a -= 26
        elif a >= 91:
            a += shift
        ciphertext += chr(a)
    if k:
        ciphertext = ciphertext.lower()
    elif k == 0:
        ciphertext = ciphertext.capitalize()
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    a = ""
    k = ""
    if ciphertext == ciphertext.lower():
        ciphertext = ciphertext.upper()
        k = 1
    elif ciphertext == ciphertext.capitalize():
        ciphertext = ciphertext.upper()
        k = 0
    for i in range(len(ciphertext)):
        a = ord(ciphertext[i])
        if a >= 65:
            a -= shift
            if a < 65:
                a += 26
        plaintext += chr(a)
    if k:
        plaintext = plaintext.lower()
    elif k == 0:
        plaintext = plaintext.capitalize()
    return plaintext

ex = encrypt_caesar("python_xz")
ex2 = decrypt_caesar('Sbwkrq3.6')
print(ex, ex2)