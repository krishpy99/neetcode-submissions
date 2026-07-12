class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        best = 0
        for i in range(len(nums)):
            dp[i][1] = nums[i]
            if i > 0:
                dp[i][0] = max(dp[i-1][1], dp[i-1][0])
                dp[i][1] = max(dp[i][1], dp[i-1][0] + nums[i])
            best = max(best, max(dp[i][0], dp[i][1]))
        
        return best