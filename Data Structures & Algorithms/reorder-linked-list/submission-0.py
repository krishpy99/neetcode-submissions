# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
        
        curhead = first.next
        first.next = None
        prev = None
        while curhead:
            tmp = curhead.next
            curhead.next = prev
            prev = curhead
            if tmp:
                curhead = tmp
            else:
                break


        new_head = ListNode()
        first = head
        turn = 0
        
        temp = new_head


        while first is not None and curhead is not None:
            if not turn%2:
                print(first.val, end="->*")
                temp.next = first
                first = first.next
            else:
                print(curhead.val, end="->*")
                temp.next = curhead
                curhead = curhead.next
            temp = temp.next
            turn += 1
        
        while first is not None:
            print(first.val, end="->+")
            temp.next = first
            first = first.next
            temp = temp.next

        while curhead is not None:
            print(curhead.val, end="->+")
            temp.next = curhead
            curhead = curhead.next
            temp = temp.next
        
