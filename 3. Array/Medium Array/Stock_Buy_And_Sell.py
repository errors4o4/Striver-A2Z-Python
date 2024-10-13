from typing import List

nums = [7, 1, 5, 3, 6, 4]


class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    mini = prices[0]
    profit = 0
    for i in range(1, len(prices)):
      cost = prices[i] - mini
      profit = max(cost, profit)
      mini = min(mini, prices[i])
    return profit


solution = Solution()
print(solution.maxProfit(nums))
