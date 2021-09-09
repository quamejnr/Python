def max_sub_array(numbers: list[int]) -> int:
    """ Finding the contiguous sub array with the largest sum"""
    first_number = numbers[0]
    max_sum = first_number
    current_sum = first_number

    remaining_numbers = numbers[1:]

    for number in remaining_numbers:
        current_sum = max(current_sum + number, number)
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    pass
