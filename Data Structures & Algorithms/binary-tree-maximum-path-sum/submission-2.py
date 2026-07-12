# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            res=[-1000000, -1000000]
            if root is None:
                return res
            a = dfs(root.left)
            b = dfs(root.right)
            res[0] = max(max(a[0], b[0]) + root.val, root.val)
            res[1] = max(a[1], max(max(b[1], a[0] + b[0] + root.val), root.val))
            return res
        
        result = dfs(root)

        return max(result[0], result[1])