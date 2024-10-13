from typing import List

nums = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3


class Solution:

  def subarraySum(self, nums: List[int], k: int) -> int:

    count = 0

    for i in range(len(nums)):
      sum = 0
      for j in range(i, len(nums)):
        sum += nums[j]
        if sum == k:
          count += 1
          
    return count


solution = Solution()
print(solution.subarraySum(nums, k))
