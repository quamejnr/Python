# from contextlib import contextmanager
import os
from send2trash import send2trash
import inflect


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
    Decrypts file using a key which is an integer.
    """

    with open(file, 'r') as f:
        text = f.read()
    with open("decrypted.txt", 'w') as nf:
        decode = ''.join(list(map(lambda x: chr(ord(x)-key), text)))
        nf.write(decode)


def search(path, keyword=''):
    """ Search for files in a path with keyword. """
    dir_list = os.listdir(path)
    dir_list.sort()
    for f in dir_list:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            search(fullname, keyword)
        elif keyword.casefold() in f.casefold():
            print(f'{f} -   ({path})')


def check(path):
    """ Returns files in folder path. """
    for folder, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            yield filename


def find(path_1, path_2):
    """ Returns common files in two different paths and gives an option to delete. """
    dir_1 = list(check(path_1))
    dir_1.sort()
    dir_2 = list(check(path_2))
    dir_2.sort()
    files = []
    p = inflect.engine()
    if len(dir_1) <= len(dir_2):
        print(path_1)
        for file in dir_1:
            mx = len(dir_2)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == dir_2[index]:
                    files.append(file)
                    print(file)
                    break
                elif file < dir_2[index]:
                    mx = index - 1
                else:
                    mn = index + 1
    else:
        print(path_2)
        for file in dir_2:
            mx = len(dir_1)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == dir_1[index]:
                    files.append(file)
                    print(file)
                    break
                elif file < dir_1[index]:
                    mx = index - 1
                else:
                    mn = index + 1
    print('')
    print(f"{len(files)} {p.plural_noun('file',len(files))} found\n")
    if len(files) == 0:
        pass
    else:
        option = input(f"Delete {p.plural_noun('file',len(files))}?\nYes\nNo\n")
        if option.casefold() in ['yes', 'y']:
            answer = input(f"Delete {p.plural_noun('file',len(files))} from:"
                           f"\n1. Path 1 - {path_1}"
                           f"\n2. Path 2 - {path_2}\n")
            if answer == str(1):
                for f in files:
                    filename = os.path.join(path_1, f)
                    send2trash(filename)
                    print('deleting file...')

                print(f"{len(files)} {p.plural_noun('file',len(files))} deleted from {path_1}\n")
            elif answer == str(2):
                for f in files:
                    filename = os.path.join(path_2, f)
                    send2trash(filename)
                    print('deleting file...')
                print(f"{len(files)} {p.plural_noun('file', len(files))} deleted from {path_2}\n")
            else:
                pass
        else:
            pass


find(r'C:\Users\Quame Junior\Downloads\Video', r'D:\\')
