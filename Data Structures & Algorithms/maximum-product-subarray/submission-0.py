class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1
        min_p = 1
        best = nums[0]
        for i in nums:
            a = max_p * i
            b = min_p * i
            c = i
            max_p = max(a, b, c)
            min_p = min(a, b, c)
            best = max(best, a, b, c)
        
        return best