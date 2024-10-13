nums = [10, 20, 30, 40, 50]
target = 25


def Ceil(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  ans = -1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] >= target):
      ans = nums[mid]
      high = mid - 1

    else:
      low = mid + 1
      
  return ans


def Floor(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  ans = -1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] <= target):
      ans = nums[mid]
      low = mid + 1

    else:
      high = mid - 1

  return ans


print(Ceil(nums, target))
print(Floor(nums, target))
