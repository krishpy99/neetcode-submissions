class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        x = 0
        b = -1000000
        for i in nums:
            x += i
            if b < x:
                b = x
            if x < 0:
                x = 0
        
        return b