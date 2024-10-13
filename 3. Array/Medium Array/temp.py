nums = [2, 5, 6, 9, 11]
target = 14

left = 0
right = len(nums) -1

while (left < right):
  
  sum = nums[left] + nums[right]

  if (sum < target):
    left += 1

  elif (sum > target):
    right -= 1

  else:
    print(left, right)
    break
