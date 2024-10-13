from typing import List

nums = 5

temp = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    n = numRows+1
    a = []
    for i in range(1, n):
      temp = []
      ans = 1
      temp.append(ans)
      
      for j in range(1, i):
        ans = ans * (i - j)
        ans = ans // j
        temp.append(ans)
      a.append(temp)
  
    return a


solution = Solution()
print(solution.generate(nums))


# def ncr_row(n):
#   res = 1
#   print(res)
#   for i in range(n):
#     res = res * (n - i)
#     res = res // (i + 1)
#     print(res)

# def ncr_col(n, r):
#   res = 1
#   for i in range(r):
#     res = res * (n - i)
#     res = res // (i + 1)
#   return res



