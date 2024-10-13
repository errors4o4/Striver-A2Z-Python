nums =[1, 2, 3, 4, 5]

a=10

def Linear(nums):
  for i in range(len(nums)):
    if nums[i] == a:
      return print(i)
  return print(-1)


Linear(nums)