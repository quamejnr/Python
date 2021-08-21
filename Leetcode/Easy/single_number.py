def single_number(nums: list[int]) -> int:
    """
    Find a unique number in an array
    :param nums: list of integers
    :return: a unique number
    """

    d = {}

    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d.setdefault(num, 1)

    for num in d:
        if d[num] == 1:
            return num


if __name__ == '__main__':
    pass
