class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x += i
        
        return (len(nums) * (len(nums) + 1) // 2) - x