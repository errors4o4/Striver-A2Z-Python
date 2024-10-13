# nums = [0, 3, 4, 7, 9, 10]
# cows = 4


# def canWePlace(nums, min_dist, cows):
#   count = 1
#   last_cow = nums[0]

#   for i in range(len(nums)):
#     if (nums[i] - last_cow) >= min_dist:
#       count += 1
#       last_cow = nums[i]

#     if (count >= cows):
#       return True

#   return False


# def agg_cow(nums, cows):
#   n = len(nums)
#   nums.sort()
#   minn = nums[0]
#   maxx = nums[n - 1]

#   for i in range(1, (maxx - minn)):

#     if (canWePlace(nums, i, cows) == True):
#       continue

#     else:
#       return i - 1


# print(agg_cow(nums, cows))



nums = [0, 3, 4, 7, 9, 10]
cows = 4


def canWePlace(nums, min_dist, cows):
  count = 1
  last_cow = nums[0]

  for i in range(len(nums)):
    if (nums[i] - last_cow) >= min_dist:
      count += 1
      last_cow = nums[i]

    if (count >= cows):
      return True

  return False


def agg_cow(nums, cows):
  n = len(nums)
  nums.sort()
  low = 0
  high = nums[n - 1] - nums[0]

  while(low<=high):

    mid = (high + low)//2
    
    if (canWePlace(nums, mid, cows) == True):
      low = mid +1

    else:
      high = mid -1

  return high


print(agg_cow(nums, cows))