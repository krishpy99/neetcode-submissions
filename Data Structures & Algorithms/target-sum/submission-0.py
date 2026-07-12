class Solution:
    def __init__(self):
        self.d = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (len(nums), target) in self.d:
            return self.d[(len(nums), target)]

        self.d[(len(nums), target)] = 0

        if len(nums) == 1:
            self.d[(len(nums), target)] = (nums[0] == target) + (nums[0] == -target)
            return self.d[(len(nums), target)]
        
        self.d[(len(nums), target)] = self.findTargetSumWays(nums[1:], target + nums[0]) + self.findTargetSumWays(nums[1:], target - nums[0])
        
        return self.d[(len(nums), target)]