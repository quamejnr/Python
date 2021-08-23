
def climbing_stairs(num):
    """Function that calculates the number of distinct ways you can climb stairs of a number of steps"""
    one, two = 1, 1
    for i in range(num-1):
        one, two = one + two, one

    return one


if __name__ == '__main__':
    pass
