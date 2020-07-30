import random
import string
# create an input (number)
# let code figure out your input (number)


def password_break2():
    """My earlier code to password break."""
    password = input("Enter password: ") # input your a number
    password = list(password)
    go_figure = []
    pos = 0

    while True:
        # random number is chosen
        num = random.randint(0, 10)

        if str(num) == password[pos]:   # number is changed to string and compared to the positional number of the input
            go_figure.append(num)
            pos = pos + 1               # the index of number is increased by one to compare next number

        if len(go_figure) == len(password):
            # when the length of the password becomes same as input
            # strings are joined and the result returned
            go_figure = "".join(map(str, go_figure))
            print(go_figure)
            break


def generate_pass(num):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(num)])


def password_break():
    """My latest function to password break."""
    password = input("Enter your password: ")
    index = 0
    new_password = []
    while len(new_password) != len(password):
        rand_letter = random.choice(string.ascii_letters+string.digits)
        if rand_letter == password[index]:
            new_password.append(rand_letter)
            index += 1
    return ''.join(new_password)

