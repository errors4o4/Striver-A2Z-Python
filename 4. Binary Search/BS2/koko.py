import math

nums= [3,7,6,11]
h = 8

def cal(nums, mid):
  totalhrs = 0

  for i in range(len(nums)):
    totalhrs += math.ceil(nums[i]/mid)

  return totalhrs


def minimumRateToEatBananas(nums, h):
  low = 1 
  high = max(nums)

  while(low<= high):
    mid = (low+high)//2
    
    totalHRS = cal(nums, mid)
    print(mid,totalHRS)

    if(totalHRS <= h):
      high = mid -1

    else:
      low = mid +1
      
  return low



print(minimumRateToEatBananas(nums, h))