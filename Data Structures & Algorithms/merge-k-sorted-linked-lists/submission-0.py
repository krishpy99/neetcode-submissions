# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergeList = ListNode()
        temp = mergeList
        flag = True
        while flag:
            x = -1
            for i, j in enumerate(lists):
                if j is not None:
                    if x == -1 or lists[x].val > j.val:
                        x = i
            
            if x == -1:
                break

            temp.next = lists[x]
            temp = temp.next
            lists[x] = lists[x].next

        return mergeList.next

