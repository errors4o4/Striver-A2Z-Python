import math

nums = [1, 2, 5, 9]
limit = 7



def sum_of_d(nums, mid):
  div_sum = 0

  for i in range(len(nums)):
    div_sum += math.ceil(nums[i]/mid)

  return div_sum


def smd(nums, limit):
  n = len(nums)

  if n > limit:
      return -1
    
  low = 1
  high = max(nums)
  

  while (low <= high):
    mid = (low + high) // 2

    print(mid , sum_of_d(nums, mid))

    if (sum_of_d(nums, mid) <= limit):
      high = mid-1

    else:
      low = mid +1

  return low
      

print(smd(nums, limit))