# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        
        x = self.dfs(root.left)
        y = self.dfs(root.right)
        if abs(y - x) > 1:
            self.flag = False
        return max(x, y) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        self.dfs(root)

        return self.flag
