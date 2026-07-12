class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i = 0
        j = 0
        while i < len(prices) and j < len(prices):
            best = max(best, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            else:
                j += 1
        return best