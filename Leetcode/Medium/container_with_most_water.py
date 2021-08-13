
def difference(right, left):
    return right - left


def max_area(height: list[int]) -> int:
    result = 0

    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * difference(right, left)
        result = max(result, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


if __name__ == '__main__':
    pass


