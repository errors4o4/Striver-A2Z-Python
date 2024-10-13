from typing import List
class Solution:
  def findmaxiConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    maxi = 0
    for i in range(len(nums)):
      if (nums[i] == 1):
        count += 1
        maxi = max(maxi, count)

      else:
        count = 0

    return print(maxi)


nums = [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
solution = Solution()
solution.findmaxiConsecutiveOnes(nums)
