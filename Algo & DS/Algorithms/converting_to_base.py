
def base_number(number, base):
    remainder_list = []

    while number >= base:
        remainder = number % base
        remainder_list.append(str(remainder))
        number = number // base

    remainder_list.append(str(number))

    return int(''.join(remainder_list[::-1]))


if __name__ == '__main__':
    pass

