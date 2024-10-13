nums = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2  # no of bouquets require 
k = 3  # no of adjacent flowers


def possible(nums, day, m ,k):
  count = 0
  noB= 0

  for i in range(len(nums)):
    if (nums[i] <= day):
      count += 1

    else:
      noB += (count/k)
      count = 0

  noB += (count/k)
  
      