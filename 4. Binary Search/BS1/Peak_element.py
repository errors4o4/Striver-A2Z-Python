nums = [1,2,3,4]


def bs(nums):
  n = len(nums)

  
  if (n==1) or (nums[0] > nums[1]):
    return 0

  if (nums[n - 2] < nums[n - 1]):
    return n - 1

  low = 1
  high = n - 2

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]):
      return mid

    if (nums[mid - 1] < nums[mid]):
      low = mid + 1

    else:
      high = mid - 1

  return -1


print(bs(nums))
