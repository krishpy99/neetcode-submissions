class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1000] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[len(nums) - 1]