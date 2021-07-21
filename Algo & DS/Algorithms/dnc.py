# Some functions to explain divide and conquer ---> Recursion
import string
import timeit
import sys


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


def is_palindrome(chars):
    """
    Checks if a word or a phrase is a palindrome
    :param chars: word or phrase (str)
    :return: True if word or phrase is a palindrome, False if otherwise
    """

    # Change characters into lower case and remove all whitespaces
    chars = ''.join([char.lower() for char in chars if char in string.ascii_letters])

    if len(chars) <= 1:
        return True
    else:
        return chars[0] == chars[-1] and is_palindrome(chars[1:-1])


def fib(n, dic):
    if n in dic:
        return dic[n]
    else:
        ans = fib(n - 1, dic) + fib(n - 2, dic)
        dic[n] = ans
        return ans


d = {1: 1, 2: 2}


def fib2(n):
    """Slower Version"""
    if n <= 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib3(n):
    """Fibonacci sequence using iteration. Uses less memory compared to recursion"""

    ans = 0

    if n == 0:
        return ans

    if n == 1:
        return 1

    elif n == 2:
        return 2

    prev2, prev1 = 1, 2

    for idx in range(3, n+1):
        ans = prev2 + prev1

        prev2, prev1 = prev1, ans

    return ans


# print(fib(400, d))
# nums = [2, 42, 5, 6, 7, 10, 2, 3, 9]

# print(total(nums))
# print(total1(nums))
# print(total2(nums))
# print(count(nums))
# print(maximum(nums))

# print(is_palindrome('Was it a car or a cat I saw?'))
#
# print(sys.getsizeof(fib3(4000)))
# print(sys.getsizeof(fib(200, d)))
