
def threeSumClosest(self, nums: list[int], target: int) -> int:
    nums.sort()
    upper_index = len(nums) - 1
    lower_index = 0
    min_difference = 'inf'

    mid_index = (upper_index + lower_index) // 2

    while lower_index <= upper_index:
        upper_three = sum(nums[mid_index: mid_index + 3])
        lower_three = sum(nums[mid_index - 2: mid_index + 1])

        upper_diff = abs(upper_three - target)
        lower_diff = abs(lower_three - target)
        if upper_diff < lower_diff:
            min_difference = upper_diff
            mid_index = lower_index

        elif upper_diff > lower_diff:
            min_difference = lower_diff
            mid_index = upper_index

    return min_difference
