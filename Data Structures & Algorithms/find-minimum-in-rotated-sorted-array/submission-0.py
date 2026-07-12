class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        minnum = nums[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            minnum = min(minnum, nums[mid])
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        minnum = min(minnum, nums[lo])
        return minnum