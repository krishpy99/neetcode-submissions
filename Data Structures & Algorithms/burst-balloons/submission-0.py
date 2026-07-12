class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def rec(i, j, left, right):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            bestcost = 0
            for k in range(i, j+1):
                cost = left * nums[k] * right
                cost += rec(i, k-1, left, nums[k])
                cost += rec(k+1, j, nums[k], right)
                
                bestcost = max(bestcost, cost)
            
            dp[(i, j)] = bestcost
            return bestcost
        
        return rec(0, len(nums) - 1, 1, 1)

