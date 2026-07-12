class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x = sum(nums)
        if x % 2:
            return False
        
        dp = [[-1 for _ in range(x//2 + 1)] for _ in nums]

        def recurse(i, sum1):
            if sum1 == 0:
                return 1
            if sum1 < 0:
                return 0
            if i >= len(nums):
                if sum1 == 0:
                    return 1
                return 0
            if dp[i][sum1] != -1:
                return dp[i][sum1]
            
            if recurse(i+1, sum1) == 1:
                dp[i][sum1] = 1
                return 1
            
            if recurse(i+1, sum1 - nums[i]) == 1:
                dp[i][sum1] = 1
                return 1
            
            dp[i][sum1] = 0
            return 0
        
        return recurse(0, x//2) == 1