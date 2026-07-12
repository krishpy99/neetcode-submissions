# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global counter
        counter = 0
        
        def dfs(root, m):
            global counter
            if root is None:
                return
            if root.val >= m:
                counter += 1
            dfs(root.left, max(root.val, m))
            dfs(root.right, max(root.val, m))
        
        dfs(root, -101)
        return counter