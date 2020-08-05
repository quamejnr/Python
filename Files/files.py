# from contextlib import contextmanager
# import os

#
# @contextmanager
# def file_manager(file, mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()
#
#
# with file_manager('text2.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)
#
# print(f.closed)
#
# @contextmanager
# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)
#
#
# with change_dir('Sample-Dir'):
#     print(os.listdir())
#     print(os.getcwd())
#
# print(os.getcwd())


def reverse_text(file, new_file):
    """Rewrites lines of text in the reverse order."""
    with open(file, 'r') as f:
        with open(new_file, 'w') as nf:
            content = f.read()
            new_content = content.split('\n')
            nf.write('\n'.join(new_content[::-1]))


# reverse_text('text.txt', 'new.txt')


def has_snake(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            if 'snake' in line:
                print(line)


def numbering(file, new_file):
    """Returns text with lines numbered."""
    with open(file, 'r') as f:
        with open(new_file, 'w') as nf:
            content = f.readlines()
            num = 1
            for line in content:
                nf.write(f'{num}. {line}')
                num += 1


def de_numbering(file, new_file):
    """Function removes the numbering of lines in a text."""
    with open(file, 'r') as f:
        with open(new_file, 'w') as nf:
            content = f.readlines()
            nums = list(range(len(content)+1))
            index = 1
            for line in content:
                if line.startswith(f'{nums[index]}.'):
                    new_content = line.strip(f"{nums[index]}. ")
                    nf.write(new_content)
                    index += 1
                else:
                    nf.write(line)


def cryptic(file, key):
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
    Decrypts file using a key which is an integer.
    """

    with open(file, 'r') as f:
        text = f.read()
    with open("decrypted.txt", 'w') as nf:
        decode = ''.join(list(map(lambda x: chr(ord(x)-key), text)))
        nf.write(decode)




