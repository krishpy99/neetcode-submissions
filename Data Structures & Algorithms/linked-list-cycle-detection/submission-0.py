# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        temp2 = head
        while temp is not None and temp2 is not None:
            temp = temp.next
            temp2 = temp2.next
            if temp2 is None:
                break
            temp2 = temp2.next
            if temp == temp2:
                return True
        
        return False