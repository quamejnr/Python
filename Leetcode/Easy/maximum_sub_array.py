
def max_sub_array(nums: list[int]) -> int:
    max_num = float('-inf')

    total = 0

    for num in nums:
        total += num
        max_num = max(total, max_num)

    return max_num


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))