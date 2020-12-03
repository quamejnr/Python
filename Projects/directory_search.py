import os
import sys

path = sys.argv[1]
keyword = sys.argv[2]


def search(path, keyword=''):
    """ Search for files in a path with keyword. """
    dir_list = os.listdir(path)
    dir_list.sort()
    for f in dir_list:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            search(fullname, keyword)
        else:
            if keyword.casefold() in f.casefold():
                print(f)


if __name__ == '__main__':
    search(path, keyword)
