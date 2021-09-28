# My Initial Solution
def remove_duplicates(nums: list[int]) -> int:
    hash_table = {}

    clone_nums = nums[:]

    count = 0

    for num in clone_nums:
        # if element already in hash table, pop element and count
        if num in hash_table:
            nums.remove(num)
            count += 1

        # if element not in hash table, add element to hash table and give it a value of 1
        else:
            hash_table[num] = 1

    # return the number of elements in the hash and the list
    return len(hash_table)


def remove_duplicates2(nums: list) -> int:

    if len(nums) == 0:
        return 0

    i = 0
    j = 1

    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)

        else:
            i += 1
            j += 1

    return j


# A newer solution by me
def remove_duplicates3(array: list[int]) -> int:
    count = 1
    i = 0
    j = 1
    l = len(array)

    if l < 1:
        return 0

    while j < l:
        if array[j] != array[i]:
            i = j
            count += 1
        j += 1

    return count


if __name__ == '__main__':
    pass
