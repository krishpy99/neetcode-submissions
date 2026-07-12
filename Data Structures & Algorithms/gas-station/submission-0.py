class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def check(i):
            tot = 0
            for ii in range(i, n):
                tot += gas[ii]
                tot -= cost[ii]
                if tot < 0:
                    return False
            
            for ii in range(0, i):
                tot += gas[ii]
                tot -= cost[ii]
                if tot < 0:
                    return False
            
            return True

        
        for i in range(n):
            if check(i):
                return i
        
        return -1