# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prevPrev = ListNode('0')
        prev = head
        if not head or not head.next:
            return head
        head = prevPrev
        curr = prev.next

        while curr:
            nex = curr.next
            prev.next = nex
            curr.next = prev
            prevPrev.next = curr

            prevPrev = prev
            prev = nex
            if not prev:
                return head.next
            curr = prev.next

        return head.next

