# Some functions to explain divide and conquer

def total(array):
    """
    Calculates the sum of elements in a list using recursive function. (My solution)

    :param array: list of elements
    :return: sum of elements in array
    """

    i = 0
    while i <= len(array):
        if len(array) == 0:
            return 0
        else:
            result = array[i] + total(array[i+1:])
            i += 1
            return result


def total1(array):
    """
    Grokking algorithms solution
    """
    if not array:
        return 0
    return array[0] + total1(array[1:])


def total2(array):
    """
    Adding the elements in a list using a for loop
    """

    total = 0
    for n in array:
        total += n
    return total


def count(array):
    """
    Counts the number of elements in an array
    """
    if not array:
        return 0
    return 1 + count(array[1:])


def maximum(array):
    """
    Returns the maximum number in a list
    """
    if not array:
        return 0
    elif array[0] > maximum(array[1:]):
        return array[0]
    return maximum(array[1:])


nums = [2, 42, 5, 6, 7, 10, 2, 3, 9]

# print(total(nums))
# print(total1(nums))
# print(total2(nums))
# print(count(nums))
print(maximum(nums))
