from typing import List

nums =[ 1,2,3,-3,1,1,1,4,2,-3]
k =3

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    mpp = {}
    presum = 0
    cnt = 0
    mpp[0] =1

    for i in range(n):
      presum += nums[i]
      mpp[presum] = mpp.get(presum, 0) + 1

      remove = presum - k
      cnt += mpp.get(remove, 0)

    return cnt            


solution = Solution()
print(solution.subarraySum(nums,k))