def max_profit(nums: list[int]) -> int:
    result = 0

    i = 0
    j = 1
    l = len(nums)

    min_num = nums[0]

    while j < l:
        if nums[j] < nums[i]:
            min_num = nums[j]
            i, j = j, j + 1
        else:
            difference = nums[j] - min_num
            result = max(result, difference)
            j += 1

    return result
