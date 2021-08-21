
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
    My Solution
    Finding all numbers in range of 1 and length of nums not in nums
    :param nums: list of integers
    :return: list of integers
    """
    missing_numbers = []

    for number in range(1, len(nums) + 1):
        if number not in nums:
            missing_numbers.append(number)

    return missing_numbers


def find_disappeared_numbers2(nums: list[int]) -> list[int]:
    """
    Optimized Solution
    Finding all numbers in range of 1 and length of nums not in nums
    
    :param nums: list of integers
    :return: list of integers
    """
    missing_numbers = []
    length = len(nums) + 1
    nums = set(nums)

    for number in range(1, length):
        if number not in nums:
            missing_numbers.append(number)

    return missing_numbers


if __name__ == '__main__':
    pass
