class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i, j in enumerate(height):
            left[i] = j
            if i > 0:
                left[i] = max(left[i-1], left[i])
        
        for i, j in enumerate(height[::-1]):
            right[i] = j
            if i > 0:
                right[i] = max(right[i-1], right[i])
        
        right = right[::-1]

        for i in range(len(height)):
            for j in range(max(height)):
                if height[i] <= j and left[i] > j and right[i] > j:
                    #print(i, j)
                    cnt += 1

        return cnt 