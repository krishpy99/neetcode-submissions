class Node:
    def __init__(self, val, nextNode):
        self.val = val
        self.next = nextNode
    

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        itr = self.head
        while itr:
            if index == 0:
                return itr.val
            itr = itr.next
            index -= 1
        
        return -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        print(self.head.val)
        self.count += 1

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            self.count += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)
        self.count += 1

    def remove(self, index: int) -> bool:
        if index >= self.count:
            return False

        if index == 0:
            if self.head:
                self.head = self.head.next
                self.count -= 1
                return True
            else:
                return False

        itr = self.head
        while index > 1:
            print(itr.val, index)
            itr = itr.next
            index -= 1
        print(itr.val, index)
        itr.next = itr.next.next
        self.count -= 1
        return True
        

    def getValues(self) -> List[int]:
        l = []
        itr = self.head
        while itr:
            l.append(itr.val)
            itr = itr.next
        return l
