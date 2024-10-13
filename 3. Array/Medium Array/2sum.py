from typing import List

print("Hello World")
target = 14
nums = [2, 6, 5, 7, 11]

class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    right, left = len(nums) - 1, 0
    nums.sort()
    
    while (left<right):
      sum = nums[left]+nums[right]
      
      if (sum == target):
        return (left, right)
        
      elif (sum < target):
        left += 1
      
      else:
        right -= 1
    return "no"

solution = Solution()
print(solution.twoSum(nums, target))
