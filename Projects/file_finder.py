"""
Program returns common files that exist in different paths and gives you the option to delete.
"""

import os
from send2trash import send2trash
import inflect


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


if __name__ == '__main__':
    find(r"F:\MOVIES", r"D:\VIDEOS\CINEMA\MOVIES")