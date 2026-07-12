class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cheapest = prices[0]
        for i in range(len(prices)):
            cheapest = min(cheapest, prices[i])
            maxprofit = max(maxprofit, prices[i] - cheapest)
        
        return maxprofit