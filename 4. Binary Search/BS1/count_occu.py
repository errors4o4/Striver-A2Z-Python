nums = [3, 4, 13, 13, 13, 20, 40]
target = 13

def lowB(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  lowb = -1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] >= target):
      lowb = mid
      high = mid - 1

    else:
      low = mid + 1

  return lowb

def uppB(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  uppb = -1

  while (low <= high):
    mid = (low + high) // 2

    if (nums[mid] > target):
      uppb = mid
      high = mid - 1

    else:
      low = mid + 1

  return uppb

def occur(nums, target, lowB, uppB):
  n = len(nums)

  lb = lowB(nums, target)

  if(lb ==n or nums[lb] != target):
    return -1,-1

  ub = uppB(nums, target)
  return ub-lb

print(occur(nums, target, lowB, uppB))