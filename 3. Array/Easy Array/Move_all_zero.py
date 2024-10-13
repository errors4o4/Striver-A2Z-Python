# nums =[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
nums =[0,1,0]
print(nums)

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      j = -1
      n = len (nums)
      # Place the pointer j
      for i in range(n):
          if nums[i] == 0:
              j = i
              break

      # No non-zero elements
      if j == -1:
          return nums

      # Move the pointers i and j and swap accordingly
      for i in range(j + 1, n):
          if nums[i] != 0:
              nums[i], nums[j] = nums[j], nums[i]
              j += 1

      return nums


moveZeroes(nums)



