nums = [
    [3, 4, 7, 9],
    [12, 13, 16, 18],
    [20, 21, 23, 29],
]


def search_2D(nums, target):
    n = len(nums)
    m = len(nums[0])

    low = 0
    high = (n * m) - 1

    while (low <= high):
        mid = (low + high) // 2

        row = mid // m
        col = mid % m

        if (nums[row][col] == target):
            return True

        elif (nums[row][col] < target):
            low = mid + 1

        else:
            high = mid - 1

    return False


print(search_2D(nums, 3))
