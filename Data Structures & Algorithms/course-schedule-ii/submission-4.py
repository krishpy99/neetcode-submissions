from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        i_o = [0 for _ in range(numCourses)]
        for i in prerequisites:
            g[i[1]].append(i[0])
            i_o[i[1]] += 1         

        def hasCycle():
            v = [0 for _ in range(numCourses)]
            in_stack = [0 for _ in range(numCourses)]

            def dfs(i):
                nonlocal v, in_stack
                if in_stack[i] == 1:
                    return True
                if v[i] == 1:
                    return False
                in_stack[i] = 1
                v[i] = 1
                for j in g[i]:
                    if dfs(j):
                        return True
                in_stack[i] = 0
                return False

            for i in range(numCourses):
                if v[i] == 0 and dfs(i):
                    return True
            
            return False
        
        if hasCycle():
            return []
        
        res = []
        v = [0 for _ in range(numCourses)]
        def dfs(i):
            nonlocal res
            v[i] = 1
            for j in g[i]:
                if v[j] != 1:
                    dfs(j)
            res.append(i)
        
        for i in range(numCourses):
            if v[i] == 0:
                dfs(i)
        
        return res[::-1]            