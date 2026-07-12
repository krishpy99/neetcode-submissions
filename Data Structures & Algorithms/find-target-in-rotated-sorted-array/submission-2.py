class Solution:
    def binsearch(self, nums, target, lo, hi):
        #print(nums[lo:hi+1], target, lo, hi)
        if lo == hi:
            if nums[lo] == target:
                return lo
            return -1
        
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:
            if target > nums[mid] or target < nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if target < nums[mid] or target > nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return self.binsearch(nums, target, lo, hi)


            
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums, target, 0, len(nums) - 1)