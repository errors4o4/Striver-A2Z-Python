from typing import List

# nums = [  # m j=col
#     [1, 2, 3, 4],  #n i=row
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]

nums = [ 
      #left  #right
# top 
      [1, 2, 3, 4],   
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10, 9, 8, 7]
# bottom
]

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    nums = matrix
    n = len(nums)
    left, right = 0, n-1  #col
    top, bottom = 0, n-1  #row

    while(top <= bottom and left <= right):
      for i in range(left, right+1):   #left, right
        print(nums[top][i])
      top += 1
      
  
      for j in range(top, bottom+1):  #top, bottom
        print(nums[j][right])
      right -= 1

      if(top<=bottom):
        for k in reversed(range(left, right+1)):  #right, left
          print(nums[bottom][k])
      bottom -= 1
  
      if(left<=right):
        for l in reversed(range(top, bottom+2)):  #bottom,top
          print(nums[l][left])
      left += 1
      

    # for i in range(n):
    #   for j in range(i, n - i):  #TOP
    #     print(nums[i][j])
    #   print(" ")

    #   for k in range(i+1, n - i):  #RIGHT
    #     print(nums[k][n - 1 - i])
    #   print(" ")

    #   for l in reversed(range(i,n-1-i)):  #BOTTOM
    #     print(nums[n - 1 - i][l])
    #   print(" ")

    #   for m in reversed(range(i+1, n-1)):  #LEFT
    #     print(nums[m][i])
    #   print(" ")


solution = Solution()
print(solution.spiralOrder(nums))
