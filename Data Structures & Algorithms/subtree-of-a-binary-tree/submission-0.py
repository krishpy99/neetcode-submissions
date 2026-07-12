# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def checkTree(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return p.val == q.val and self.checkTree(p.left, q.left) and self.checkTree(p.right, q.right)
    
    def dfs(self, p, q):
        if self.checkTree(p, q):
            self.flag = True
            return
        if p is None:
            return
        self.dfs(p.left, q)
        self.dfs(p.right, q)
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        self.dfs(root, subRoot)
        return self.flag