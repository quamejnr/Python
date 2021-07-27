
def base_number(number, base):
    remainder_list = []

    while number >= base:
        remainder = number % base
        remainder_list.append(str(remainder))
        number = number // base

    remainder_list.append(str(number))

    return int(''.join(remainder_list[::-1]))


def base_number_rec(n, base):
    """ Prints a number in the base provided. """
    if n > 1:
        base_number_rec(n//base, base)
    remainder = n % base
    print(remainder, end='')


if __name__ == '__main__':
    base_number_rec(20, 2)

