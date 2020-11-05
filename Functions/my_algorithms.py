import heapq
import random
import string
import inflect
import os
from functools import cache
import timeit


def odd_or_even(arr):
    """Function to return if the sum of an array is even or odd."""
    if sum(arr) % 2 == 0 or sum == 0:
        return 'even'
    return 'odd'


def mask(cc):
    """Function to replace all but the last 4 characters of your input with '#'."""
    anon = len(cc[:-4]) * "#"
    new_str = f'{anon}{cc[-4:]}'
    return new_str


def iq_test(numbers):
    """Function to check if a number in a string differs from others in terms of evenness and return its index
    Indices of array starts with 1."""
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
    """Finding the sum for all the multiples of 3 and 5 below the number passed in."""
    result = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    return sum(result)


def solution2(number):
    """Finding the sum of all the multiples of 3 and 5 below the number passed in (Faster solution)."""
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result


def disemvowel(text):
    """Removing vowels from strings."""
    return ''.join([letter for letter in text if letter.lower() not in 'aeiou'])


def disemvowel1(text):
    vowels = "aeiou"
    sans_vowel = ''
    for i in text:
        if i.lower() not in vowels:
            sans_vowel += i
    return sans_vowel


def is_valid_walk(walk):
    """A walk around a city block that takes exactly 10 minutes and returns you to where you started."""
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')


def rgb(r, g, b):
    """Return hex code of colours (Function Incomplete)."""
    hex_code = {0: '0', 1: '1', 2: '2', 3: '3',
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

        inverse = code[::-1]
        new_code = [hex_code.get(key) for key in inverse]
        return "".join(new_code)
    return '0' * 6


def find_nb(m):
    """Finding number of cubes for building a pile of cubes given the volume of cube."""
    n, res = 1, 1
    while res < m:
        n += 1
        res += n**3
    return n if res == m else -1


def random_nums(num, mn, mx):
    """Function for generating random numbers."""
    array = []
    while len(array) < num:
        array.append(random.randrange(mn, mx))
    return array


def rand_lst(num, mn, mx):
    """Function for generating random numbers."""
    lst = []
    for i in range(num):
        rand_num = random.randrange(mn, mx)
        lst.append(rand_num)
    return lst


def distinct_rand_nums(num, mn, mx):
    """Function for generating distinct random numbers."""
    lst = list(range(mn, mx))
    random.shuffle(lst)
    return lst[:num]


def distinct_rand_nums2(num, mn, mx):
    """Function for generating distinct random numbers (Faster code)."""
    lst = []
    while len(lst) < num:
        rand_num = random.randrange(mn, mx)
        if rand_num not in lst:
            lst.append(rand_num)
    return lst


def queue_time1(customers, n):
    """queue time taken for customers to check-out of the supermarket given the number of checkout tills(n)."""
    if len(customers) != 0:
        new_lst, b = sorted(customers[:n]), customers[n:]
        for i in b:
            new_lst[0] += i
            new_lst = sorted(new_lst)
        return new_lst[-1]
    return 0


def queue_time2(customers, n):
    """Faster alternate code to previous code."""
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)


def cryptic(msg):
    """This function encrypts messages by changing them to ASCII codes."""
    code = []
    for word in msg.split(' '):
        new_msg = [ord(char) for char in word]
        code.append(new_msg)
    return code


def decrypt(code):
    """This function decrypts ASCII codes into English."""
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


def spin_words(sentence):
    """Function that takes one or more strings and returns the inverse of a word with five or more letters."""
    sentence = sentence.split()
    new_sentence = []
    for word in sentence:
        if len(word) >= 5:
            word = word[::-1]
            new_sentence.append(word)
        else:
            new_sentence.append(word)
    return " ".join(new_sentence)


def unique_in_order(iterable):
    """Function to return a unique order of lists of letters, eg. a list of 'AAAABBBCCDAABBB' returns 'ABCDAB' """
    i = None
    new_lst = []
    for letter in iterable:
        if letter != i:
            new_lst.append(letter)
            i = letter
    return new_lst


def tickets(people):
    counter = 0
    deck = []
    for person in people:
        if person > 25:
            change = person - 25
            if counter < change:
                return "NO"
            elif counter >= change:
                if change == 25:
                    if 25 in deck:
                        deck.remove(25)
                        counter -= change
                        counter += person
                        deck.append(person)
                    else:
                        return 'NO'
                elif change == 75:
                    if (deck.count(25) == 3) and (50 not in deck):
                        for i in range(3):
                            deck.remove(25)
                        counter -= change
                        counter += person
                        deck.append(person)
                    elif (25 in deck) and (50 in deck):
                        deck.remove(25)
                        deck.remove(50)
                        counter -= change
                        counter += person
                        deck.append(person)

                    else:
                        return 'NO'
        else:
            counter += person
            deck.append(person)

    return "YES"


def tickets2(people):
    """Simpler code to previous code."""
    till = {100.0: 0, 50.0: 0, 25.0: 0}

    for paid in people:
        till[paid] += 1
        change = paid - 25.0

        for bill in (50, 25):
            while bill <= change and till[bill] > 0:
                till[bill] -= 1
                change -= bill

        if change != 0:
            return 'NO'

    return 'YES'


def generate_pass(num):
    """Function to generate a random password."""

    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(num)])


def password_break():
    """Takes input of password and figures out password.

    Limitation: this can only figure out numbers only passwords.
    Will be suitable for breaking safes and phone passwords
    """
    password = input("Enter password: ")
    password = list(password)
    go_figure = []
    pos = 0

    while True:
        num = random.randint(0, 10)

        if str(num) == password[pos]:
            go_figure.append(num)
            pos = pos + 1

        if len(go_figure) == len(password):
            go_figure = "".join(map(str, go_figure))
            print(go_figure)
            break


def password_break2():
    """Takes input of password and figures out password.

    This function solves the limitation of the earlier code thus can break any password.
    """

    password = input("Enter your password: ")
    index = 0
    new_password = []
    count = 0
    while len(new_password) != len(password):
        rand_letter = random.choice(string.ascii_letters + string.digits + ' _-')
        if rand_letter == password[index]:
            new_password.append(rand_letter)
            index += 1
        count += 1
    return ''.join(new_password), count


def merge(lst1, lst2):
    """Returns only items present in both lists of two sorted lists."""
    x1 = 0
    x2 = 0
    result = []
    while True:
        if x1 == len(lst1):
            return result

        elif x2 == len(lst2):
            return result

        elif lst1[x1] == lst2[x2]:
            result.append(lst1[x1])
            x1 += 1

        elif lst1[x1] < lst2[x2]:
            x1 += 1

        else:
            x2 += 1


def present1(lst1, lst2):
    """
    Returns only elements present in a first list of
    two sorted lists but not in the second list.

    """
    x1 = 0
    x2 = 0
    result = []
    while True:
        if x1 == len(lst1):
            return result

        elif x2 == len(lst2):
            result.extend(lst1[x1:])
            return result

        elif lst1[x1] == lst2[x2]:
            x1 += 1

        elif lst1[x1] < lst2[x2]:
            result.append(lst1[x1])
            x1 += 1

        else:
            x2 += 1


def bagdiff(lst1, lst2):
    """
    Returns items from the first list of two sorted lists
    that are not eliminated by a matching element in the second list.

    """
    x1 = 0
    x2 = 0
    result = []
    while True:
        if x1 == len(lst1):
            result.extend(lst2[x2:])
            return result

        elif x2 == len(lst2):
            result.extend(lst1[x1:])
            return result

        elif lst1[x1] == lst2[x2]:
            x1 += 1
            x2 += 1

        elif lst1[x1] < lst2[x2]:
            result.append(lst1[x1])
            x1 += 1

        else:
            result.append(lst2[x2])
            x2 += 1


def reverse(lst):
    """Returns a list in the reversed form."""
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
    return lst


def counting_letters(sentence):
    """Returns each character in a sentence and the number of times it appears in the sentence."""

    count = {}

    for char in sentence:
        count.setdefault(char, 0)
        count[char] += 1
    return count


def binary_search(array, target):

    p = inflect.engine()          # Used for formatting

    mx = len(array)
    mn = 0
    counter = 1
    while mn <= mx:
        index = (mx + mn)//2
        if target == array[index]:
            return f"Found {target} in {counter} {p.plural_noun('try', counter)}"
        if target < array[index]:
            mx = index - 1
            counter += 1
        if target > array[index]:
            mn = index + 1
            counter += 1
    return -1


def base_num(num, base):
    """ Returns a number in the base provided. """
    lst = []
    while num >= base:
        remainder = num % base
        lst.append(remainder)
        num = num // base
    lst.append(num)
    lst.reverse()
    result = map(str, lst)
    return ''.join(result)


def ctb(n, base):
    """ Returns a number in the base provided. """
    if n > 1:
        ctb(n//base, base)
    print(n % base)


def display(path):
    """ Search for files in a path with keyword. """
    dir_list = os.listdir(path)
    dir_list2 = os.listdir('C:\\Users\\Quame Junior\\Downloads\\Video')
    dir_list.sort()
    dir_list2.sort()
    for f in dir_list:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            display(fullname)
        else:
            print(f)


def compare(path, path2):
    """ Delete files in multiple places. """
    dir_list = os.listdir(path)
    dir_list2 = os.listdir(path2)
    dir_list.sort()
    dir_list2.sort()
    for f in dir_list:
        fullname = os.path.join(path, f)
        fullname2 = os.path.join(path2, f)
        if os.path.isdir(fullname):
            compare(fullname, path2)
        elif f in dir_list2:
            # deletes file permanently
            # os.unlink(fullname2)
            print(f)


def check(path):
    for folder, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            yield filename


def find2(path_1, path_2):
    path_1 = list(check(path_1))
    path_1.sort()
    path_2 = list(check(path_2))
    path_2.sort()
    for file in path_1:
        if file in path_2:
            print(file)


def find(path_1, path_2):
    """ Faster code to earlier code using binary search"""
    path_1 = list(check(path_1))
    path_1.sort()
    path_2 = list(check(path_2))
    path_2.sort()
    if len(path_1) <= len(path_2):
        for file in path_1:
            mx = len(path_2)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == path_2[index]:
                    print(file)
                    break
                elif file < path_2[index]:
                    mx = index - 1
                else:
                    mn = index + 1
    else:
        for file in path_2:
            mx = len(path_1)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == path_1[index]:
                    print(file)
                    break
                elif file < path_1[index]:
                    mx = index - 1
                else:
                    mn = index + 1
