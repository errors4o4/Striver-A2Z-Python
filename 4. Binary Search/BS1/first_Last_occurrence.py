# nums = [3, 4, 13, 13, 13, 20, 40]
# target = 13

# def lowB(nums, target):
#   n = len(nums)
#   low = 0
#   high = n - 1
#   lowb = -1

#   while (low <= high):
#     mid = (low + high) // 2

#     if (nums[mid] >= target):
#       lowb = mid
#       high = mid - 1

#     else:
#       low = mid + 1

#   return lowb

# def uppB(nums, target):
#   n = len(nums)
#   low = 0
#   high = n - 1
#   uppb = -1

#   while (low <= high):
#     mid = (low + high) // 2

#     if (nums[mid] > target):
#       uppb = mid
#       high = mid - 1

#     else:
#       low = mid + 1

#   return uppb

# def occur(nums, target, lowB, uppB):
#   n = len(nums)

#   lb = lowB(nums, target)

#   if(lb ==n or nums[lb] != target):
#     return -1,-1

#   return lb, uppB(nums, target)-1

# print(occur(nums, target, lowB, uppB))

nums = [2, 8, 8, 8, 8, 8, 11, 13]
target = 14


def occu(nums, target):
  n = len(nums)
  low = 0
  high = n - 1
  first = -1

  while low <= high:
    mid = (low + high) // 2

    if (nums[mid] == target):
      first = mid
      high = mid - 1

    elif (nums[mid] < target):
      low = mid + 1

    else:
      high = mid - 1

  if(first == -1): 
    return (first, -1)
      

  low = 0
  high = n - 1
  last = -1

  while low <= high:
    mid = (low + high) // 2

    if (nums[mid] == target):
      last = mid
      low = mid + 1

    elif (nums[mid] < target):
      low = mid + 1

    else:
      high = mid - 1

  return first, last


print(occu(nums, target))
