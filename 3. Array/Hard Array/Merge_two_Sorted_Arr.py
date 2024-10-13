from typing import List

n = 4
nums1 = [1, 3, 5, 7]
m = 5
nums2 = [0, 2, 6, 8, 9]



# class Solution:

#   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     i = n -1
#     j = 0

#     while (i>=0 and j < m):
#       if (nums1[i] > nums2[j]):
#         nums1[i], nums2[j] = nums2[j], nums1[i]
#         j += 1
#         i -= 1
#       else: 
#         break

#     nums1.sort()
#     nums2.sort()
      
#     return nums1, nums2


class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    ans = [0] * (n + m)
    i, j = 0, 0
    index = 0

    while (i < n and j < m):

      if (i == 0 or nums1[i] <= nums2[j]):
        ans[index] = nums1[i]
        i += 1
        index += 1

      elif (j == 0 or nums1[i] > nums2[j]):
        ans[index] = nums2[j]
        j += 1
        index += 1

    while (i < n):
      ans[index] = nums1[i]
      i += 1
      index += 1

    while (j < m):
      ans[index] = nums2[j]
      j += 1
      index += 1

    for i in range(n + m):
      if i < n:
        nums1[i] = ans[i]
      else:
        nums2[i - n] = ans[i]

    return nums1, nums2

solution = Solution()
print(solution.merge(nums1, m, nums2, n))
