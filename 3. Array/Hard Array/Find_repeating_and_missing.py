
nums = [4,3,6,2,1,1]

def mis(nums):
  n= len(nums)
  ans = [0]*(n+1)

  for i in range(n):
    ans[nums[i]] = ans[nums[i]] + 1

  for j in range(1,len(ans)):
    if ans[j] == 2:
      rep = j
    elif ans[j] ==0:
      mis = j

  return rep, mis

print(mis(nums))