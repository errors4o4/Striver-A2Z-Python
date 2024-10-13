nums = [
    [4, 2, 5, 1, 4, 5],
    [2, 9, 3, 2, 3, 2],
    [3, 6, 9, 16, 22],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2],
]


def findMaxInd(nums, n, m, col): 
  maxVal = -1
  index = -1

  for i in range(n):
    if (nums[i][col] > maxVal):
      maxVal = nums[i][col]
      index = i

  return index


def findPeakGrid(nums):
  n = len(nums)
  m = len(nums[0])
  low = 0
  high = m - 1

  while (low <= high):
    mid = (low + high) // 2
    maxRowInd = findMaxInd(nums, n, m, mid)

    left = mid - 1 >= 0 if nums[maxRowInd][mid - 1] else -1
    right = mid + 1 < m if nums[maxRowInd][mid + 1] else -1

    if (left < nums[maxRowInd][mid] and nums[maxRowInd][mid] > right):
      return (maxRowInd, mid)

    elif (left > nums[maxRowInd][mid]):
      high = mid - 1

    else:
      low = mid + 1

  return (-1, -1)


print(findPeakGrid(nums))