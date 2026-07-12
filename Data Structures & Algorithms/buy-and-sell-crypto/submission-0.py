class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices.copy()
        for i in range(1, len(minp)):
            minp[i] = min(minp[i], minp[i-1])

        best = 0
        for i in range(len(minp)):
            best = max(best, prices[i] - minp[i])
        return best