# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curhead = head
        prev = None
        while curhead:
            tmp = curhead.next
            curhead.next = prev
            prev = curhead
            if tmp:
                curhead = tmp
            else:
                return curhead
        return curhead
        