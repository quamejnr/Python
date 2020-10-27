"""
File encryption functions.
"""


def encrypt(file, key):
    """
    Encrypts file using a key which is an integer.

    :param

    file = file to be decrypted

    key = Key is an integer between 0-9
    """

    with open(file, 'r') as f:
        text = f.read()
    with open('encrypted.txt', 'w') as nf:
        try:
            code = ''.join(list(map(lambda x: chr(ord(x)+key), text)))
            nf.write(code)
        except UnicodeError as e:
            print(e)


def decrypt(file, key):
    """
    Decrypts files encrypted by previous code.
    """

    with open(file, 'r') as f:
        text = f.read()
    with open("decrypted.txt", 'w') as nf:
        decode = ''.join(list(map(lambda x: chr(ord(x)-key), text)))
        nf.write(decode)



