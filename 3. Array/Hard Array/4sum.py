from typing import List

nums = [1, 2, -1, -2, 2, 0, -1]
target = 0

class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    
    n = len(nums)
    ans = set()

    for i in range(n):
      if (i > 0 and nums[i] == nums[i - 1]):
        continue

      for j in range(i+1, n):
        if (j > i+1 and nums[i] == nums[i - 1]):
          continue
        
        k = j + 1
        M = n - 1
  
        while (k < M):
          sum = nums[i] + nums[j] + nums[k] + nums[M]
  
          if (sum < target):
            k += 1
          elif (sum > target):
            M -= 1
          else:
            temp = [nums[i], nums[j], nums[k], nums[M]]
            ans.add(tuple(temp))
            k += 1
            M -= 1
            while (k < M and nums[k] == nums[k - 1]):
              k += 1
            while (k < M  and  nums[M] == nums[M + 1] ):
              M -= 1

    return list(ans)


solution = Solution()
print(solution.fourSum(nums, target))
