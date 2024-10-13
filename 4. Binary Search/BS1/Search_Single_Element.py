# nums=[0, 1, 2, 3, 4, 5, 6, 7, 8]
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]


def bs(nums):
  n = len(nums)
  if (n == 1):
    return nums[0]

  if (nums[0] != nums[1]):
    return nums[0]

  if (nums[n - 1] != nums[n - 2]):
    return nums[n - 1]

  low = 1
  high = n - 2

  while (low <= high):
    mid = (low + high) // 2

    print(low, mid, high)
    if (nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]):
      return nums[mid]

    if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0
                                            and nums[mid] == nums[mid + 1]):
      low = mid + 1

    else:
      high = mid - 1

  return -1


print(bs(nums))
