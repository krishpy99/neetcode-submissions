# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print(preorder, inorder)
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        rootind = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                rootind = i
                break
            
        root.left = self.buildTree(preorder[1:rootind + 1], inorder[:rootind])
        root.right = self.buildTree(preorder[rootind + 1:], inorder[rootind + 1:])
        return root
