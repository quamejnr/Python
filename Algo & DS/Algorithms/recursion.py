""" Recursion """


def factorial(n):
    print(f"I'm calculating Factorial({n})")
    if n == 0:
        return 1
    ans = n * factorial(n-1)
    print(f'Done calculating Factorial({n}) - {ans}')
    return ans


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)


def is_even(x):

    if x % 2 == 0:
        return True
    return False


def power2(x, n):
    """
    Using another method to find the power.
    x^n can be written as x^(n/2) * x^(n/2) for even numbers and x * x^(n-1)
    if n is odd.
    This takes logarithmic time - O(log n)
    """
    if n == 0:
        return 1
    elif is_even(n):
        ans = power2(x, n/2)
        return ans * ans

    return x * power2(x, n-1)
