# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = [root]
        cur = 0
        r = ""
        while len(q) - cur > 0:
            if q[cur] is None:
                r+=",null"
                cur += 1
                continue
            r += "," +str(q[cur].val)
            q.append(q[cur].left)
            q.append(q[cur].right)
            cur += 1
        return r[1:]


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        r = data.split(",")
        q = [[None, None]]
        cur = 0
        c = 0
        d = {}
        while len(r) - c > 0:
            print(c, cur, r[c], r[c] == 'null')
            if c < len(r) and r[c] != 'null':
                q[cur][0] = TreeNode(r[c])
                if q[cur][1] is not None:
                    if q[cur][2] == 'L':
                        q[cur][1].left = q[cur][0]
                    else:
                        q[cur][1].right = q[cur][0]
                q.append([None, q[cur][0], 'L'])
                q.append([None, q[cur][0], 'R'])
            c += 1
            cur += 1
            for i in q:
                if i[0] is not None:
                    print(i[0].val, end=" ")
                else:
                    print(None, end=" ")
            print()

        return q[0][0]