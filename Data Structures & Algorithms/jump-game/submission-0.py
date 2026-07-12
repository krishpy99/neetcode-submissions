class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        while i <= j and i < len(nums):
            j = max(j, i + nums[i])
            i += 1
        
        return j >= len(nums) - 1