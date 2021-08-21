
def climbing_stairs(num):
    one, two = 1, 1
    for i in range(num-1):
        one, two = one + two, one

    return one


if __name__ == '__main__':
    pass
