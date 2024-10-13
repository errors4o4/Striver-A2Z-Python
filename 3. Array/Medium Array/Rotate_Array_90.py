from typing import List

nums = [  # m j=col
    [1, 2, 3, 4],  #n i=row
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    matrix = nums

    n = len(nums)

    for i in range(n):
      for j in range(i,n):
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    for row in range(len(nums)):
      nums[row].reverse()
      print(nums[row])
    

solution = Solution()
print(solution.rotate(nums))
