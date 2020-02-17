from Decorators.Decorators import my_timer
import time

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
nums = '22 2 4 9 12 10'
def iq_test(numbers):
    new = numbers.split(' ')
    odd = [index for index, value in enumerate(new, start=1) if int(value) % 2 != 0]
    even = [index for index, value in enumerate(new, start=1) if int(value) % 2 == 0]

    if len(odd) < len(even):
        for i in odd:
            return i
    else:
        for i in even:
            return i


# finding the sum of all the multiples of 3 and 5 below the number passed in
@my_timer
def solution(number):
    result = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    return sum(result)


@my_timer
def solution(number):   # Faster
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result


# Removing vowels from strings
def disemvowel(string):
    return ''.join([letter for letter in string if letter.lower() not in 'aeiou'])


# a walk around a city block that takes exactly 10 minutes and returns you to where you started
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')



