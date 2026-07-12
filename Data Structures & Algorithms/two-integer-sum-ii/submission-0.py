class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i):
                if numbers[i] + numbers[j] == target:
                    return [j + 1, i + 1]
        return []