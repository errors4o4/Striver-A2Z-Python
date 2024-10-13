nums = [3,4,5,1,2]

import sys


def bs(nums):
  n = len(nums)
  low = 0
  high = n - 1
  mini = sys.maxsize
  index = -1

  while (low <= high):
    mid = (low + high) // 2

    # If search space is already sorted,
    if nums[low] <= nums[high]:
      if nums[low] < mini:
          index = low
          mini = nums[low]
      break

    # Check if left list is sorted
    if (nums[low] <= nums[mid]):
      mini = min(mini, nums[low])
      low = mid + 1

    # Check if right list is sorted
    else:
      mini = min(mini, nums[mid])
      high = mid - 1

  return index


print(bs(nums))
