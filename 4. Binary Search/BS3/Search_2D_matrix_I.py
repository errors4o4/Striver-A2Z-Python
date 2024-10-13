nums = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]


def search_2D(nums, target):
    n = len(nums)
    m = len(nums[0])

    row = 0
    col = m - 1

    while (row < n and col >= 0):
        mid = nums[row][col]

        if (mid == target):
            return print(row, col)

        elif (mid < target):
            row += 1

        else:
            col -= 1

    return False


print(search_2D(nums, 3))
