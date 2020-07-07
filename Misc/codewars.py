from Decorators.Decorators import my_timer
import heapq
import random


def odd_or_even(arr):
    """function to return if the sum of an array is even or odd"""
    if sum(arr) % 2 == 0 or sum == 0:
        return 'even'
    return 'odd'


def maskify(cc):
    """function to replace all but the last 4 characters of your input with"""
    anon = len(cc[:-4]) * "#"
    new_str = f'{anon}{cc[-4:]}'
    return new_str


def iq_test(numbers):
    """function to check if a number in a string differs from others in terms of evenness and return its index
    Indices of array starts with 1"""
    new = numbers.split(' ')
    odd = [index for index, value in enumerate(new, start=1) if int(value) % 2 != 0]
    even = [index for index, value in enumerate(new, start=1) if int(value) % 2 == 0]

    if len(odd) < len(even):
        for i in odd:
            return i
    else:
        for i in even:
            return i


def solution(number):
    """finding the sum of all the multiples of 3 and 5 below the number passed in"""
    result = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    return sum(result)


def solution2(number):
    """finding the sum of all the multiples of 3 and 5 below the number passed in
    (Faster solution)"""
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result


def disemvowel(string):
    """Removing vowels from strings"""
    return ''.join([letter for letter in string if letter.lower() not in 'aeiou'])


def is_valid_walk(walk):
    """a walk around a city block that takes exactly 10 minutes and returns you to where you started"""
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')


def rgb(r, g, b):
    """Return hex code of colours (Function Incomplete)"""
    hex = {0: '0', 1: '1', 2: '2', 3: '3',
           4: '4', 5: '5', 6: '6', 7: '7',
           8: '8', 9: '9', 10: 'A', 11: 'B',
           12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    code = []
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


def find_nb(m):
    """finding number of cubes for building a pile of cubes given the volume of cube"""
    n, res = 1, 1
    while res < m:
        n += 1
        res += n**3
    return n if res == m else -1


def random_nums(num):
    """Function for generating random numbers"""
    array = []
    while len(array) < num:
        array.append(random.randint(1, 20))
        return array


def queue_time1(customers, n):
    """queue time taken for customers to check-out of the supermarket given the number of checkout tills"""
    if len(customers) != 0:
        new_lst, b = sorted(customers[:n]), customers[n:]
        for i in b:
            new_lst[0] += i
            new_lst = sorted(new_lst)
        return new_lst[-1]
    return 0


print(queue_time1([5, 8, 4, 2], 2))

def queue_time2(customers, n):
    """faster alternate code to previous code"""
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)


def cryptic(msg):
    """This function encrypts messages by changing them to ASCII codes"""
    code = []
    for word in msg.split(' '):
        new_msg = [ord(char) for char in word]
        code.append(new_msg)
    return code


def decrypt(code):
    """This function decrypts ASCII codes into English"""
    word = []
    for lst in code:
        asc = [chr(x) for x in lst]
        word.append(''.join(asc))
    return ' '.join(word)


def create_phone_number(n):
    k = ''.join([str(x) for x in n])
    return f'({k[:3]}) {k[3:6]}-{k[6:]}'


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# print(cryptic("The Lord is good"))
# a = decrypt(cryptic("The Lord is good"))
# print(a)
