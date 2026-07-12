class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        d = {}
        for i in hand:
            d[i] = d.get(i, 0) + 1

        i = min(hand)
        while i != -1:
            x = d[i]
            j = i
            newi = -1
            while j < i + groupSize:
                if j not in d:
                    #print(j)
                    return False
                d[j] -= x
                if d[j] == 0:
                    del d[j]
                else:
                    if newi == -1:
                        newi = j
                j += 1
            if newi == -1 and len(d) > 0:
                newi = min(d.keys())
            i = newi

        return True