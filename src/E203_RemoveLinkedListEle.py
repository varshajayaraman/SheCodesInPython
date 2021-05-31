# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return

        while head and head.val == val:
            head = head.next
        t = head

        while t:
            while t.next and t.next.val != val:
                t = t.next
            if t.next is None:
                break
            t.next = t.next.next
        return head