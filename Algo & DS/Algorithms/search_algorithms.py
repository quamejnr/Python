
def linear_search(lst, target):
    """
    :param lst: data list
    :param target: the object being searched for in the data list
    :return: index of object if found else None
    """

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return None


def verify(ind):
    if ind is not None:
        print('Target found at index:', ind)
    else:
        print("Target not found")


numbers = [i for i in range(100000)]

print('Linear search\n------------')
result = linear_search(numbers, 12000)
verify(result)

result = linear_search(numbers,3)
verify(result)


def binary_search(lst, target):
    """
    :param lst: data list
    :param target: the object being searched for in the data list
    :return: index of object if found else None
    """

    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last)//2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


print('\nBinary search\n------------')
result = binary_search(numbers, 12000)
verify(result)

result = binary_search(numbers,3)
verify(result)


def recursive_binary_search(lst, target):
    """
    :param lst: data list
    :param target: the object being searched for in the data list
    :return: True if object in the list, False if not
    """

    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst)//2

        if lst[midpoint] == target:
            return True
        elif lst[midpoint] < target:
            return recursive_binary_search(lst[midpoint+1:], target)
        else:
            return recursive_binary_search(lst[:midpoint], target)


print('\nRecursive Binary search\n------------')
result = recursive_binary_search(numbers, 12000000000)
print(result)