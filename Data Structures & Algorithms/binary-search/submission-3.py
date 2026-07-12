class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        
        if nums[l] == target:
            return l
        
        return -1