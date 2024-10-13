from typing import List

nums = [2, 1, 1, 1, 3, 1, 4, 5, 6, 2]


class Solution:

  def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    cnt1, cnt2 = 0, 0  # counts
    el1, el2 = float('-inf'), float('-inf')  # element 1 and element 2

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
      if cnt1 == 0 and el2 != nums[i]:
        cnt1 = 1
        el1 = nums[i]
        
      elif cnt2 == 0 and el1 != nums[i]:
        cnt2 = 1
        el2 = nums[i]
        
      elif nums[i] == el1:
        cnt1 += 1
        
      elif nums[i] == el2:
        cnt2 += 1
        
      else:
        cnt1 -= 1
        cnt2 -= 1

    ans = []
    cnt1, cnt2 = 0, 0
    
    for i in range(n):
      if nums[i] == el1:
        cnt1 += 1
      if nums[i] == el2:
        cnt2 += 1

    mini = n // 3
    
    if cnt1 > mini:
      ans.append(el1)
    if cnt2 > mini:
      ans.append(el2)

    return ans


# class Solution:
#   def majorityElement(self, nums: List[int]) -> List[int]:

#     ans = []
#     mp = {}
#     n = len(nums)
#     count = 0

#     for i in range(n):

#       if nums[i] in mp:
#         count += 1
#         mp[nums[i]] = count
#       else:
#         count = 1
#         mp[nums[i]] = count

#       if (mp[nums[i]] > n//3):
#         ans.append(nums[i])

#     return ans

solution = Solution()
print(solution.majorityElement(nums))
