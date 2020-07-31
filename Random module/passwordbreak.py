import random
import string


def password_break():
    """
    Takes input of password and makes random combinations to figure out code.
    Limitation: Can only break passwords with only numbers
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
    """My latest function to password break. Solves the limitation in the earlier function"""

    password = input("Enter your password: ")
    index = 0
    new_password = []
    while len(new_password) != len(password):
        rand_letter = random.choice(string.ascii_letters + string.digits + ' _-')
        if rand_letter == password[index]:
            new_password.append(rand_letter)
            index += 1
    return ''.join(new_password)


def generate_password(num):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(num)])
