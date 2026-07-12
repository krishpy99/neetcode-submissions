# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        d = {}
        def dfs(root, parent, vNode) -> bool:
            if root is None:
                return False
            if root.val == vNode.val:
                d[root.val] = d.get(root.val, 0) + 1
                return True
            if dfs(root.left, root, vNode):
                d[root.val] = d.get(root.val, 0) + 1
                return True
            if dfs(root.right, root, vNode):
                d[root.val] = d.get(root.val, 0) + 1
                return True
            
            return False
        
        dfs(root, root, p)
        dfs(root, root, q)

        for i in d.keys():
            if d[i] == 2:
                return TreeNode(i)
        
        return TreeNode()