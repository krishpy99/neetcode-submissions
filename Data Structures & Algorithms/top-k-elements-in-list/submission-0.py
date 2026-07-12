class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        l = []
        cnt = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i-1]:
                l.append([cnt, nums[i-1]])
                cnt = 0
            cnt += 1
        l.append([cnt, nums[-1]])
        l = sorted(l, reverse = True)
        res = []
        for i in range(k):
            res.append(l[i][1])
        return res


