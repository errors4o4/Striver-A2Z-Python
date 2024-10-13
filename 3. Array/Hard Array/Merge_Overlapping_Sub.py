from typing import List

nums = [[1, 3], [2, 4], [2, 6], [8, 9], [8, 10], [9, 11], [15, 18], [16, 17]]


class Solution:

  def merge(self, nums: List[List[int]]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []

    for i in range(n):
      if (not ans or nums[i][0] > ans[-1][1]):
        ans.append(nums[i])

      else:
        ans[-1][1] = max(ans[-1][1], nums[i][1])
        
   
    return ans


# class Solution:

#   def merge(self, nums: List[List[int]]) -> List[List[int]]:
#     n = len(nums)
#     nums.sort()
#     ans = []

#     for i in range(n):
#       start = nums[i][0]
#       end = nums[i][1]

#       if (len(ans) != 0 and end <= ans[-1][1]):
#         continue

#       for j in range(i + 1, n):
#         if (nums[j][0] <= end):
#           end = max(end, nums[j][1])

#         else:
#           break

#       ans.append([start, end])

#     return ans

solution = Solution()
print(solution.merge(nums))
