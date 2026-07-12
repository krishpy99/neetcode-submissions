# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        prev = None
        while n > 1:
            n -= 1
            temp2 = temp2.next
        
        while temp2 is not None and temp2.next is not None:
            temp2 = temp2.next
            prev = temp1
            temp1 = temp1.next
        
        #print(temp2.val, temp1.val)
        if temp1 == head:
            head = head.next
        else:
            prev.next = temp1.next

        return head