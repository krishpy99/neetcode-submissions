# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur = 0
        if root is None:
            return []
        q = [[root, 1]]
        
        while len(q) - cur > 0:
            curr = q[cur]

            if curr[1] > len(res):
                res.append([curr[0].val])
            else:
                res[-1].append(curr[0].val)
            if curr[0].left is not None:
                q.append([curr[0].left, curr[1] + 1])
            if curr[0].right is not None:
                q.append([curr[0].right, curr[1] + 1])
            cur += 1
        
        return res