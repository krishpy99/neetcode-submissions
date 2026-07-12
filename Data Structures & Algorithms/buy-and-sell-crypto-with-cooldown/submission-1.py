class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in prices]

        for i, j in enumerate(prices):
            if i > 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + j)
            if i > 1:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - j)
            else:
                dp[i][1] -= j
                if i > 0:
                    dp[i][1] = max(dp[i][1], dp[i-1][1])
        
        #for i in dp:
            #print(i[0], i[1])
            
        return max(dp[-1][0], dp[-1][1])