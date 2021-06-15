import time
import random

def min_number(array):
    smallest_index = 0
    smallest = array[smallest_index]

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    """
    Selection sort sorts elements in a list by removing the smallest element in an array and appending to a new list
    :param array:
    :return: a sorted list
    """

    sorted_list = []

    # find smallest index of array and pop
    for i in range(len(array)):
        smallest_index = min_number(array)
        sorted_list.append(array.pop(smallest_index))

    return sorted_list


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


numbers = [4, 2, 1, 5, 6, 12, 8, 9, 19, 8]


def rin():
    nums = []
    for _ in range(100000):
        nums.append(random.randint(1, 1000))
    return nums

# print(rin())

numb = rin()

tic = time.perf_counter()
print('starting quicksort...')
quicksort(numb)
toc = time.perf_counter()
print(f"{toc-tic:0.4f}")


# tic = time.perf_counter()
# print('starting selection sort...')
# selection_sort(rin())
# toc = time.perf_counter()
# print(f"{toc-tic:0.4f}")

