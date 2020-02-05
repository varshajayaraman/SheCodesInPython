class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp = self.head
        if not temp:
            return -1
        i = 0
        while i < index:
            if not temp.next:
                return -1
            temp = temp.next
            i += 1
        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = self.head
        if not temp:
            self.head = ListNode(val)
            return
        while temp.next:
            # print(temp.next.val)
            temp = temp.next
        temp.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        temp = ListNode(val)
        t = self.head
        if index == 0:
            temp.next = self.head
            self.head = temp

        else:
            i = 0
            while i + 1 < index:
                if t.next:
                    t = t.next
                    i += 1
                else:
                    return
            temp.next = t.next
            t.next = temp
            print("Add at index: ", self.head)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        temp = self.head
        if not temp:
            return
        if index == 0:
            self.head = self.head.next
        i = 0
        while i + 1 < index:
            if temp.next:
                temp = temp.next
                i += 1
            else:
                return

        if not temp.next:
            return
        temp.next = temp.next.next
        print("Delete: ", self.head)
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)