nums = [3, 4, 6, 7, 9, 10, 16, 17]
target = 10


def low_b(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  ans = n

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] > target):
      ans = mid
      high = mid -1

    else:
      low = mid + 1

  return ans

print(low_b(nums, target))
