def square_root(number) -> float:
    return number ** 0.5


def is_factor(dividend, divisor) -> bool:
    return dividend % divisor == 0


def is_prime(number) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True

    upper_bound = int(square_root(number) + 1)
    lower_bound = 2
    for num in range(lower_bound, upper_bound):
        if is_factor(number, num):
            return False

    return True


if __name__ == "__main__":
    pass

