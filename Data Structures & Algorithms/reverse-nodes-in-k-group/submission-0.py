# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseUntilZero(self, node, val):
        if node is None:
            return None, None, None
        
        #return node, node, node.next
        print(node.val, val)

        if val == 0:
            return node, node, node.next
        
        start, end, after = self.reverseUntilZero(node.next, val - 1)

        if start is None or end is None:
            return None, None, None
            
        end.next = node
        
        return start, node, after


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = ListNode()
        newHead.next = head
        temp = newHead
        while True:
            start, end, next_start = self.reverseUntilZero(temp.next, k - 1)
            if start is None:
                #print(newHead)
                break
            
            temp.next = start
            end.next = next_start
            temp = end
        
        #print(newHead.next)
        
        return newHead.next