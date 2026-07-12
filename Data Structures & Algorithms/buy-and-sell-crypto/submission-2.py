class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        pd = {}
        for i in range(len(prices)):
            pd[i] = prices[i]
            for j in pd.values():
                maxprofit = max(maxprofit, prices[i] - j)
        
        return maxprofit