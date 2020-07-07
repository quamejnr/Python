
lst = [4, 3, 9, 12, 21, 1, 3]


# functions to find the max number without using max function in the library (faster code)

def max_num(nums):
    # sorts list and returns the last number in list
    new_nums = sorted(lst)
    return new_nums[-1]


def max_num2(nums):
    max_number = 0  # 0 is assigned to max number
    for num in nums:
        if num > max_number:
            # for each number in list, if number is greater than preceding number
            # Number becomes max number
            max_number = num
    return max_number



