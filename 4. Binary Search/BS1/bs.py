nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6


def bs(nums, low, high, target):
  if (low > high):
    return -1

  mid = (low + high) // 2

  if (nums[mid] == target):
    return mid

  elif (nums[mid] < target):
    return bs(nums, mid + 1, high, target)

  else:
    return bs(nums, low, mid - 1, target)


def bs(nums, target):
  n = len(nums)
  low = 0
  high = n - 1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] == target):
      return mid

    elif (target < nums[mid]):
      high = mid - 1

    else:
      low = mid + 1

  return -1

  
# print(bs(nums, 0, len(nums) - 1, target))
print(bs(nums, target))