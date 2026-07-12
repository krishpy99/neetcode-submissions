# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        res = ListNode()
        r = res
        while l1 is not None and l2 is not None:
            r.next = ListNode((l1.val + l2.val + c) % 10)
            c = (l1.val + l2.val + c) // 10
            l1 = l1.next
            l2 = l2.next
            r = r.next
        
        while l1 is not None:
            r.next = ListNode((l1.val + c) % 10)
            c = (l1.val + c) // 10
            l1 = l1.next
            r = r.next

        while l2 is not None:
            r.next = ListNode((l2.val + c) % 10)
            c = (l2.val + c) // 10
            l2 = l2.next
            r = r.next
        
        if c > 0:
            r.next = ListNode(c)
        
        return res.next