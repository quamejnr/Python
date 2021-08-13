
def remove_element(nums: list, val: int):

    i = 0

    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            nums.pop(i)

    return i


if __name__ == "__main__":
    pass


