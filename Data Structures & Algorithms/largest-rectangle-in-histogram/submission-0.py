class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = []
        stack = []
        for i, j in enumerate(heights):
            while len(stack) > 0 and stack[-1][0] >= j:
                stack.pop()
        
            if len(stack) == 0:
                left.append(-1)
            else:
                left.append(stack[-1][1])
        
            stack.append([j, i])
        
        right = []
        stack = []
        for i, j in enumerate(heights[::-1]):
            while len(stack) > 0 and stack[-1][0] >= j:
                stack.pop()
        
            if len(stack) == 0:
                right.append(len(heights))
            else:
                right.append(stack[-1][1])
        
            stack.append([j, len(heights) - i - 1])
        
        right = right[::-1]
        best = 0

        for i, j in enumerate(heights):
            best = max(best, j * (right[i] - left[i] - 1))
        print(left)
        print(right)
        return best    