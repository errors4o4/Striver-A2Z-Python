m = 4
nums = [25, 46, 28, 49, 24]


# pages_std is number of pages allocated to student
# add pages_std + num[i] if its under the pages count then we add the it to pages_std
# else  go to next student and set pages_std = num[i]
# return how many students can handle the pages in list
def countPainters(nums, time):
  painters = 1
  boardsPainter = 0

  for i in range(len(nums)):
    if (boardsPainter + nums[i] <= time):
      boardsPainter += nums[i]

    else:
      painters += 1
      boardsPainter = nums[i]

  return painters


# m = total num of stud
# calulate no_std if no_std > m then go to right side else go to left side
def findLargestMinDistance(m, nums):
  n = len(nums)

  if (m > n):
    return -1

  low = max(nums)
  high = sum(nums)

  while (low <= high):
    mid = (low + high) // 2
    painters = countPainters(nums, mid)

    if (painters > m):
      low = mid + 1

    else:
      high = mid - 1

  return low


print(findLargestMinDistance(m, nums))
