nums = [10, 22, 12, 3, 0, 6]
a = []

a.append(nums[len(nums) - 1])
maxNum = 0

for i in range(len(nums) - 2, -1, -1):
  if nums[i] > a[maxNum]:
    a.append(nums[i])
    maxNum += 1

print(a)
