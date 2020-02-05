"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        temp = head
        if not temp:
            head = Node(insertVal, None)
            head.next = head
            return head

        while temp:
            if temp.val == insertVal:
                t = Node(insertVal, temp.next)
                temp.next = t
                return head
            elif temp.next:
                if temp.val < insertVal and temp.next.val >= insertVal:
                    t = Node(insertVal, temp.next)
                    temp.next = t
                    return head
                elif temp.val < insertVal and temp.next.val < temp.val and temp.next.val < insertVal:
                    t = Node(insertVal, temp.next)
                    temp.next = t
                    return head
                elif temp.val > insertVal and temp.next.val < temp.val and temp.next.val >= insertVal:
                    t = Node(insertVal, temp.next)
                    temp.next = t
                    return head
                else:
                    if temp.next == head:
                        t = Node(insertVal, temp.next)
                        temp.next = t
                        return head
                    else:
                        temp = temp.next
        return head