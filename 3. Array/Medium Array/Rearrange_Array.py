from typing import List

nums = [-1, -2, -3, 1, 2, 3]


class Solution:

  def rearrangeArray(self, nums: List[int]) -> List[int]:
    a = [0]*(len(nums))
    
    pos = 0
    neg = 1
    for i in range(len(nums)):

      
      if (nums[i] > 0):
        a[pos] = nums[i]
        pos += 2

      else:
        a[neg] = nums[i]
        neg += 2
        
    return a


solution = Solution()
print(solution.rearrangeArray(nums))
