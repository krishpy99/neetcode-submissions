class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        setter = set()
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                #print(i, j, nums[i], nums[j])
                t = - nums[i] - nums[j]
                low = j + 1
                high = len(nums) - 1
                #print(i, j, nums[i], nums[j], t, nums[low], nums[high])
                if t < nums[low] or t > nums[high]: continue
                #print(low, high, t, '-d')
                while low < high:
                    mid = (low + high + 1) // 2
                    if nums[mid] > t:
                        high = mid - 1
                    else:
                        low = mid

                ap = [nums[i], nums[j], t]
                if nums[low] == t and tuple(ap) not in setter:
                    res.append([nums[i], nums[j], t])
                    setter.add(tuple(ap))
        return res     