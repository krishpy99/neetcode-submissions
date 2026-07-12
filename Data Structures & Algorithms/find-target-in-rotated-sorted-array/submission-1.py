class Solution:
    def binsearch(self, nums, target, lo, hi):
        print(nums, target, lo, hi)
        if lo >= hi:
            if nums[lo] == target:
                return lo
            else:
                return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            if nums[hi] < target:
                hi -= 1
            else:
                lo = mid + 1
        else:
            if nums[lo] > target:
                lo += 1
            else:
                hi = mid - 1
        
        return self.binsearch(nums, target, lo, hi)

            
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums, target, 0, len(nums) - 1)