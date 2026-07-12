# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        tmp = head
        while list1 is not None and list2 is not None:
            if list2.val < list1.val:
                print(list1.val, list2.val, tmp.val)
                tmp.next = list2
                list2 = list2.next
            else:
                print(list1.val, list2.val, tmp.val)
                tmp.next = list1
                list1 = list1.next
            tmp = tmp.next
        while list1 is not None:
            tmp.next = list1
            list1 = list1.next
            tmp = tmp.next
        while list2 is not None:
            tmp.next = list2
            list2 = list2.next
            tmp = tmp.next
        head = head.next
        return head