#OPTIMAL

from typing import List
import sys

nums = [102, 4, 100, 101, 1, 3, 2, 1, 1]

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0

    longest = 1
    hashset= set()
    
    for i in range(len(nums)):
      hashset.add(nums[i])

    for j in hashset:
      if j -1 not in hashset:
        count = 1
        x = j
        
        while x+1  in hashset:
          x+=1
          count+=1
          
        longest = max(longest, count)

    return longest


solution = Solution()
print(solution.longestConsecutive(nums))
