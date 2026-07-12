# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.prev = -10001

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if self.isValidBST(root.left) == False:
            return False
        
        if self.prev >= root.val:
            return False
        
        self.prev = root.val

        if self.isValidBST(root.right) == False:
            return False
        
        return True