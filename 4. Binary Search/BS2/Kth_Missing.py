nums = [2, 3, 4, 7, 11]
k = 5


def kth(nums, k):
  n = len(nums)
  low = 0
  high = n - 1

  while (low <= high):
    mid = (low + high) // 2
    missing = nums[mid] - (mid + 1)

    if (missing < k):
      low = mid + 1

    else:
      high = mid -1 

  return high + k +1
  # return low + k 

print(kth(nums, k))