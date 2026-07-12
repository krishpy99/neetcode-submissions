# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root) -> int:
        if root is None:
            return 0
        
        x = self.depth(root.left)
        y = self.depth(root.right)
        self.val = max(self.val, x + y)
        return max(x, y) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        self.depth(root)
        return self.val
        
