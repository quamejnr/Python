
def binary_search(array: list, target):
    lower_index = 0
    upper_index = len(array) - 1

    while lower_index <= upper_index:

        mid_index = (upper_index + lower_index)//2

        if target == array[mid_index]:
            return mid_index

        if target > array[mid_index]:
            lower_index = mid_index + 1

        if target < array[mid_index]:
            upper_index = mid_index - 1

    return -1


def binary_search_rec(array, low, high, target):

    if low <= high:

        mid_index = (high + low)//2

        if target == array[mid_index]:
            return mid_index

        if target > array[mid_index]:
            return binary_search_rec(array, mid_index+1, high, target)

        if target < array[mid_index]:
            return binary_search_rec(array, low, mid_index-1, target)

    return -1


def occurrence(array: list, target, first: bool):
    lower_index = 0
    upper_index = len(array) - 1
    result = -1

    while lower_index <= upper_index:

        mid_index = (upper_index + lower_index)//2

        if target == array[mid_index]:
            result = mid_index
            if first:
                upper_index = result - 1
            else:
                lower_index = result + 1

        if target > array[mid_index]:
            lower_index = mid_index + 1

        if target < array[mid_index]:
            upper_index = mid_index - 1

    return result


def count_occurrences(array, number):
    first_occurrence = occurrence(array, number, first=True)
    last_occurrence = occurrence(array, number, first=False)

    if (first_occurrence or last_occurrence) >= 0:
        return (last_occurrence - first_occurrence) + 1
    return -1


def finding_rotated_times(array):
    lower_index = 0
    upper_index = len(array) - 1
    min_number = array[upper_index]
    rotated_times = upper_index

    while lower_index <= upper_index:

        mid_index = (upper_index + lower_index) // 2
        middle_number = array[mid_index]

        if middle_number < min_number:
            rotated_times = mid_index
            upper_index = mid_index - 1

        if middle_number > min_number:
            lower_index = mid_index + 1

    return rotated_times


if __name__ == '__main__':
    pass
