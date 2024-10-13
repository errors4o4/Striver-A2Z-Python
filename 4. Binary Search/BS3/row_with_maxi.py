nums = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
]


def low_b(nums, m, target):
  low = 0
  high = m - 1
  ans = m

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] >= target):
      ans = mid
      high = mid - 1

    else:
      low = mid + 1

  return ans


def Row_W_max_el(nums):
  n = len(nums)
  m = len(nums[0])

  cnt_max = 0
  index = -1

  for i in range(n):
    cnt_ones = m - low_b(nums[i], m, 1)

    if (cnt_ones > cnt_max):
      cnt_max = cnt_ones
      index = i

  return index


print(Row_W_max_el(nums))
