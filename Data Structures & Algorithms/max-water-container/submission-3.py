class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maxarea = 0
        while left < right:
            maxarea = max(maxarea, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                temp = heights[left]
                while left < right and heights[left] <= temp:
                    left += 1
            else:
                temp = heights[right]
                while right > left and heights[right] <= temp:
                    right -= 1
        
        return maxarea

