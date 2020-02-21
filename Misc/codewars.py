from Decorators.Decorators import my_timer
import time
import heapq

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


def rgb(r, g, b):
    hex ={0: '0', 1: '1', 2: '2', 3: '3',
          4: '4', 5: '5', 6: '6', 7: '7',
          8: '8', 9: '9', 10: 'A', 11: 'B',
          12: 'C', 13: 'D', 14: 'E', 15: 'F'}


    code=[]

    if all([r, g, b]):

        while r > 16:
            num = r % 16
            code.append(num)
            r = r//16
        code.append(r)

        while g > 16:
            num = g % 16
            code.append(num)
            g = g//16
        code.append(g)

        while b > 16:
            num = b % 16
            code.append(num)
            b = b//16
        code.append(b)

        reverse = code[::-1]
        new_code = [hex.get(key) for key in reverse]
        return "".join(new_code)
    return '0' * 6

# finding number of cubes for building a pile of cubes given the volume of cube

def find_nb(m):
    n, res = 1, 1
    while res < m:
        n += 1
        res += n**3
    return n if res == m else -1


import random
array = []

while len(array)<300000:
    array.append(random.randint(1, 20))

array = array


# queue time taken for customers to check-out of the supermarket given the number of checkout tills
@my_timer
def queue_time1(customers, n):
    if len(customers) != 0:
        new_lst, b = sorted(customers[:n]), customers[n:]
        for i in b:
            new_lst[0] += i
            new_lst = sorted(new_lst)
        return new_lst[-1]
    return 0


# alternate code to previous code and faster
def queue_time2(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)




