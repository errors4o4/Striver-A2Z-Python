from typing import List

nums = [-2, -3, 4, -1, -2, 1, 5, -3]


class Solution:

  def maxSubArray(self, nums: List[int]) -> int:
    sum = 0
    maxi = 0

    for i in range(len(nums)):

      if (sum == 0):
        start = i
      
      sum += nums[i]

      if (sum>maxi):
        maxi = sum
        ansStart = start
        ansEnd = i
      
      if sum < 0:
        sum = 0

    return nums[ansStart:ansEnd+1]


solution = Solution()
print(solution.maxSubArray(nums))
