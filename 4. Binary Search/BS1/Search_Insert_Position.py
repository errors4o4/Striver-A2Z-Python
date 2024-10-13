nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 9

def ins(nums, target):
  n = len(nums)
  low = 0
  high = n-1
  pos  = 0

  while(low<=high):
    mid = (low + high) // 2

    if (nums[mid]>=target):
      pos = mid
      high = mid -1

    else: 
      low = mid + 1

  return pos


print(ins(nums, target))



