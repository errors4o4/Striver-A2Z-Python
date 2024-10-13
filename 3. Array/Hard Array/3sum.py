from typing import List

nums = [-2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2]


class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:

    nums.sort()
    ans = set()


    for i in range(len(nums)):
      if (i > 0 and nums[i] == nums[i - 1]):
        continue

      j = i + 1
      k = len(nums) - 1

      while (j < k):
        sum = nums[i] + nums[j] + nums[k]
        if (sum < 0):
          j += 1
        elif (sum > 0):
          k -= 1
        else:
          temp = [nums[i], nums[j], nums[k]]
          ans.add(tuple(temp))

          j += 1
          k -= 1

          while (j < k and nums[j] == nums[j - 1]):
            j += 1
          while (j < k and nums[k] == nums[k + 1]):
            k -= 1

    return list(ans)


solution = Solution()
print(solution.threeSum(nums))
