import random
# create an input (number)
# let code figure out your input (number)

password = input("Enter numbers: ") # input your a number

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





