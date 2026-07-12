"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        print("node:", node)
        d = {}
        v = set()
        
        def clone_node(node):
            dupe_node = Node(node.val)
            d[node] = dupe_node

        def dfs(root):
            nonlocal v
            clone_node(root)
            for i in root.neighbors:
                if i not in d:
                    dfs(i)
                d[root].neighbors.append(d[i])

        dfs(node)
        return d[node]