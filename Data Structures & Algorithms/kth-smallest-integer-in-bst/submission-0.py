# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global counter
        counter = 1
        global answer
        answer = -1
        def dfs(root):
            global counter, answer
            if root is None:
                return
            dfs(root.left)
            if counter == k:
                answer = root.val
            counter += 1
            dfs(root.right)
        
        dfs(root)
        return answer