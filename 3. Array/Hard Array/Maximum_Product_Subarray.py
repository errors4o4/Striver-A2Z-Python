from typing import List


class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    prefix = 1
    suffix = 1
    maxi = float('-inf')
    n = len(nums)

    for i in range(n):
      if (prefix == 0):
        prefix = 1
      if (suffix == 0):
        suffix = 1

      prefix *= nums[i]      
      suffix *= nums[n-i-1]      

      maxi = max(maxi, max(suffix, prefix))

    return maxi


nums = [1,2,3,4,5,0]
solution = Solution()
print(solution.maxProduct(nums))