
def decimal_to_binary(number):
    remainder_list = []

    while number >= 2:
        remainder = number % 2
        number = number // 2
        remainder_list.append(str(remainder))
    remainder_list.append(str(number))
    return int(''.join(remainder_list[::-1]))


if __name__ == "__main__":
    pass
