N = 5
nums= [1,2,4,5]

def mis(nums, n):
  sum = 0
  cal = 0
  
  for i in range(len(nums)):
    sum += nums[i]

  for j in range(n+1):
    cal += j

  return cal-sum

print(mis(nums, N))