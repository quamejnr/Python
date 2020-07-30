import sys
import string
import random


def test(did_pass):
    """Function to test my functions."""
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = f'Test in {line_num} ok'
    else:
        msg = f"Test in {line_num} FAILED"

    print(msg)


def turn_clockwise(dir):
    """Function that shows you the next clockwise direction of your current direction."""
    compass = ['N', 'E', 'S', 'W']
    if dir in compass:
        if compass.index(dir) + 1 != len(compass):
            return compass[compass.index(dir) + 1]
        return compass[0]


def day_name(num):
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
    if num in range(7):
        return days[num]


def day_add(day, num):
    """Function to return the day after adding a number of days to your current day."""
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
    for k,v in days.items():
        if v == day:
            num += k
            while num >= 7:
                num -= 7
    return days[num]


def test_suite():
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")


def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        return "Invalid argument"


def sum_nums(lst):
    """Function to return the sum of a range of numbers."""
    counter = 0
    for i in lst:
        counter += i
    return counter


def sum_nums_below(lst):
    """Function to return the sum of a range of numbers (Faster code)."""
    return int((lst[-1]*(lst[-1]+1))/2)


def collatz(num):
    while num > 1:
        print(num, end=', ')
        if num % 2 == 0:
            num = num//2
        else:
            num = (num * 3) + 1
    print(num, end='.')


def length(num):
    """Function to return number of digits of a number."""
    count = 0
    while num != 0:
        count += 1
        num = num//10
    return count


def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
            n = n // 10
    return count


def range_num(n, start=0, step=1):
    num = start
    lst = []
    while num < n:
        lst.append(num)
        num += step
    return lst


def multiples(n, stop, start=1):
    for i in range(start, stop+1):
        print(n*i, end='    ')
    print()


def multi_table(stop, start=1):
    for i in range(start, stop+1):
        multiples(i, stop)


friends = [("Bliss", 19), ("Gail", 24), ("Kwame", 23), ("2d'z", 30), ("Sconza", 18), ("Kwaku", 16), ("Jeff Wellz", 17)]

# print([nm for (nm, yr) in friends if yr < 20])
# for nm, yr in friends:
#     lst = []
#     if yr < 25:
#         print(nm)


def sqrt(num):
    """Function to find square roots of numbers using Newton's method."""
    approx = num/8.0
    while True:
        better = (approx + num/approx)/2
        if abs(better - approx) < 0.001:
            return round(better, 2)
        approx = better


def is_prime(n):
    """Function to determine if a number is a prime number."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_pass(num):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(num)])


julia_more_info = ( ("Julia", "Roberts"), (8, "October", 1967),
                    "Actress", ("Atlanta", "Georgia"),
                    [("Duplicity", 2009),
                    ("Notting Hill", 1999),
                    ("Pretty Woman", 1990),
                    ("Erin Brockovich", 2000),
                    ("Eat Pray Love", 2010),
                    ("Mona Lisa Smile", 2003),
                    ("Oceans Twelve", 2004)])

#
# import turtle
#
# turtle.setup(400,500) # Determine the window size
# wn = turtle.Screen() # Get a reference to the window
# wn.title("Handling keypresses!") # Change the window title
# wn.bgcolor("lightgreen") # Set the background color
# tess = turtle.Turtle() # Create our favorite turtle
# # The next four functions are our "event handlers".
# def h1():
#     tess.forward(30)
#
# def h2():
#     tess.left(90)
#
# def h3():
#     tess.right(90)
#
# def h4():
#     wn.bye() # Close down the turtle window
#
# def h5(x, y):
#     tess.goto(x,y)
#
# # These lines "wire up" keypresses to the handlers we’ve defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
# wn.onclick(h5)
# # Now we need to tell the window to start listening for events,
# # If any of the keys that we’re monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.mainloop()



fam = ["Brother", 'Sister', 'Sis Adwoa', "Sis Akua", 'Sis Rose', 'Sis Diana', 'Bella']
# relation = ["Brother", 'Sister', 'Sis Adwoa', "Sis Akua", 'Sis Rose', 'Sis Diana', 'Bella']

# relation = fam.copy()

fam.remove("Brother")
fam.insert(3, "Mark")
fam.sort()
# print(fam)
# print(relation)

nums = [1, 2, 3, 4, 5, 6]

import turtle
# tess = turtle.Turtle()



def multiply1(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2


def multiply(lst):
    for i, val in enumerate(lst):
        lst[i] = val**2

import random

a =random.randrange(0.0, 6 )
c = random.randint(0, 1)
b = random.Random(123).randrange(0, 6)
d = list(range(10))
random.Random(5).shuffle(d)

text = "Well, I never!, said Alice."

sub = text.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’\\",
                     "abcdefghijklmnopqrstuvwxyz                                          ")


cleaned = text.translate(sub)

s1 = [6, 2, 2, 5, 5, 2, 8, 6, 9, 3, 6, 4, 7, 1, 3, 6, 7, 10]
s1.sort()
s2 = [6, 7, 7, 7, 2, 9, 3, 4, 6, 1, 6]



lst_1 = [1, 2, 4, 5, 6]
lst_2 = [1, 2, 4, 6, 5]
lst_3 = []
lst_3.append(lst_1)
# print(len(lst_3))
# lst_3.append(lst_2)
# # print(lst_3)
# print(len(lst_3))
def merge(lst1, lst2):
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


def sort_lst(lst):
    result =[]
    while len(lst) > 0:
        mn = float('inf')
        for i in lst:
            if i < mn:
                mn = i
        result.append(mn)
        lst.remove(mn)
    return result


def sort_lst2(lst):
    for i in range(len(lst)):
        min_index = i                                    # min_index is the index of the minimum number
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

# def sort_lst2(lst):
#     # min_index = 0
#     # min_num =lst[min_index]
#     for i in range(len(lst)):
#         min_num = lst[i]
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[i]:
#                 min_num = lst[j]


numbers = [2, 4,6,1,36,4, 10, 4, 8, 5]

# for i in range(0, len(numbers) - 1):
#     for j in range(0, len(numbers) - 1 - i):
#         numbers[j], numbers[j+1] = numbers[j+1], numbers[j]



import math



# a = sort_lst(numbers)
# print(a)
# sort_lst2(numbers)
# print(numbers)
# print(s2)


# print(bagdiff([5,7,11,11,11,12,13], [7,8,11]))
# print(bagdiff(s1, s2))
# print(present1(s1, s2))



