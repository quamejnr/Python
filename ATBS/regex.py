import re
from colorama import Back, Style

"""
SOME COMMON METHODS OF RE OBJECTS:

pattern.match by default searches only the beginning of the string
pattern.search searches the whole string and returns the first pattern it matches unless specified
pattern.findall returns all the matching pattern as a list
pattern.finditer returns all the matching pattern as objects
"""

with open("data.txt", 'r') as f:
    data = f.read()


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


name_pattern = re.compile(r'^[A-Z][a-z]*.*', flags=re.M)
num_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

phone_nums = num_pattern.findall(data)
names = name_pattern.findall(data)

contacts = list(zip(names, phone_nums))


def get_contact():
    """ Displays the contacts of all possible names after being given a name. """
    search = input('Contact Name:')
    for name, number in contacts:
        if search.casefold() in name.casefold():
            print(f"{name}: {number}")

    # TODO: display a message when name not in contacts
