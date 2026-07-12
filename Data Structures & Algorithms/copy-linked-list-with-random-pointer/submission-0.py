"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyHead = Node(0)
        temp = copyHead
        temp2 = head
        while temp2 is not None:
            temp.next = Node(temp2.val)
            temp2 = temp2.next
            temp = temp.next
        
        temp2 = copyHead.next
        temp = head
        while temp2 is not None:
            temp4 = copyHead.next
            temp3 = head
            while temp3 != temp.random:
                temp4 = temp4.next
                temp3 = temp3.next
            
            temp2.random = temp4

            temp2 = temp2.next
            temp = temp.next
        
        return copyHead.next

        