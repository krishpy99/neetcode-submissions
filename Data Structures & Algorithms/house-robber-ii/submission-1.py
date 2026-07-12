class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        b = 0
        for i in range(len(nums)):
            if i == 0:
                dp[i][1] = nums[0]
                continue
            dp[i][0] = nums[i]
            if i > 1:
                dp[i][0] = max(dp[i][0], dp[i-2][0] + nums[i])
                dp[i][1] = max(dp[i][1], dp[i-2][1] + nums[i])
            if i > 2:
                dp[i][0] = max(dp[i][0], dp[i-3][0] + nums[i])
                dp[i][1] = max(dp[i][1], dp[i-3][1] + nums[i])
            if i != len(nums) - 1:
                b = max(dp[i][1], b)
            b = max(dp[i][0], b)
        
        return max(b, nums[0])