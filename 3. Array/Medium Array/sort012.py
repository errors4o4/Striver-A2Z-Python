from typing import List

nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]

class Solution:

  def sortColors(self, nums: List[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1

    while (mid <= high):

      if (nums[mid] == 0):
        nums[mid], nums[low] = nums[low], nums[mid]
        low += 1
        mid += 1

      elif (nums[mid] == 1):
        mid += 1

      else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
        
    return nums


solution = Solution()
print(solution.sortColors(nums))
