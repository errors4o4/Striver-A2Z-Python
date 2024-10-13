# print("Hello World")
nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
target = 1


def bs(nums, target):
  n = len(nums)
  low = 0
  high = n - 1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] == target):
      return mid

    if (nums[low] == nums[mid] and nums[mid] == nums[high]):
      low += 1
      high -= 1
      continue

    # Check if left list is sorted
    if (nums[low] <= nums[mid]):
      if (nums[low] <= target and target <= nums[mid]):
        high = mid - 1

      else:
        low = mid + 1

    # Check if right list is sorted
    else:
      if (nums[mid] <= target and target <= nums[high]):
        low = mid + 1

      else:
        high = mid - 1

  return -1


print(bs(nums, target))