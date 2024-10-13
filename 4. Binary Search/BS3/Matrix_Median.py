# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING
# NOT WORKING

nums = [
    [1, 5, 7, 9, 11],
    [2, 3, 4, 5, 10],
    [9, 10, 12, 14, 16],
]


def upp_b(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  ans = n

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] > target):
      ans = mid
      high = mid - 1

    else:
      low = mid + 1

  return ans


def blackBox(nums, m, x):
  cnt = 0

  for i in range(m):
    cnt += upp_b(nums[i], x)

  return cnt


def Mat_Med(nums):
  n = len(nums)
  m = len(nums[0])

  low = float('inf')
  high = float('-inf')

  for i in range(m):
    low = min(low, nums[i][0])
    high = max(high, nums[i][n - 1])

  req = (n * m) // 2
  while (low <= high):
    mid = (low + high) // 2
    small_eq = blackBox(nums, m, mid)

    if small_eq <= req:
      low = mid + 1

    else:
      high = mid - 1

  return low


print(Mat_Med(nums))
