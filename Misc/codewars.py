# function to return if the sum of an array is even or odd
def odd_or_even(arr):
    if sum(arr) % 2 == 0 or sum == 0:
        return 'even'
    return 'odd'


# function to replace all but the last 4 characters of your input with #
def maskify(cc):
    anon = len(cc[:-4]) * "#"
    new_str = f'{anon}{cc[-4:]}'
    return new_str


# function to check if a number in a string differs from others in terms of evenness and return its index
# Indices of array starts with 1

def iq_test(numbers):
    new = numbers.split(' ')
    odd = [index for index, value in enumerate(new) if int(value) % 2 != 0]
    even = [index for index, value in enumerate(new) if int(value) % 2 == 0]

    if len(odd) < len(even):
        for i in odd:
            return i + 1
    else:
        for i in even:
            return i + 1
