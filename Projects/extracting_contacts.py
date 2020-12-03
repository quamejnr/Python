"""
Program extracts contact details from text
"""

import re
from colorama import Back, Style
import sys

NUMBER = re.compile(r'\d{3}-\d{3}-\d{4}|\+\d{12}|0\d{9}')
NAME = re.compile(r'[A-Z][a-z]+ ([A-Z][a-z]*-?[A-Z][a-z]+|[A-Z][a-z]+( [A-Z][a-z]+)?[^\s.])')
EMAIL = re.compile(r'[\w.]+@([a-z]+)\.([a-z]+\.[a-z]+|[a-z]+)')


def highlight_regex(pattern, text, print_output=True):
    """Returns text with all found patterns highlighted."""
    output = text
    len_inc = 0
    for match in pattern.finditer(text):
        start, end = match.start() + len_inc, match.end() + len_inc
        output = output[:start] + Back.CYAN + Style.DIM + output[start:end] + Style.RESET_ALL + output[end:]
        len_inc = len(output) - len(text)

    if print_output:
        print(output)
    else:
        return output


file = sys.argv[1]


def get_contact(file):
    """
    Displays the contacts of all possible names in the data.

    Parameters
    ----------
        file : str
            location of file containing data

    Returns
    -------
    None
    """

    with open(file, 'r') as f:
        data = f.read()

    name_pattern = re.compile(r'^[A-Z][a-z]*.*', flags=re.M)
    num_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

    phone_nums = num_pattern.findall(data)
    names = name_pattern.findall(data)

    contacts = list(zip(names, phone_nums))
    search = input('Contact Name:')
    for name, number in contacts:
        if search.casefold() in name.casefold():
            print(f"{name}: {number}")

    # TODO: display a message when name not in contacts


if __name__ == '__main__':
    get_contact(file)
