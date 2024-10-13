from typing import List

nums = [2, 2, 1, 1, 1, 2, 2]


class Solution:

  def majorityElement(self, nums: List[int]) -> int:
    count = 0
    ele = int

    for i in range(len(nums)):
      if (count == 0):
        count += 1
        ele = nums[i]

      elif (ele == nums[i]):
        count += 1

      else:
        count -= 1

    count1 = 0

    for j in range(len(nums)):
      if (nums[j] == ele):
        count1 += 1

    if (count1 > len(nums) // 2):
      return ele

  # def majorityElement(self, nums: List[int]) -> int:
  #   a = {}
  #   a = dict.fromkeys(nums, 0)

  #   for i in range(len(nums)):
  #     a[nums[i]] += 1

  #   for key, value in enumerate(a):
  #     if a[value] > (len(nums) / 2):
  #       return value


solution = Solution()
print(solution.majorityElement(nums))
