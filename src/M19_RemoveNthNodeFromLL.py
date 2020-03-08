# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = ListNode(0)
        d.next = head
        head = d
        fp, sp = head, head
        if not head or n == 0:
            return head

        # n-=1
        while n > 0 and fp.next:
            fp = fp.next
            n -= 1

        while fp.next:
            sp = sp.next
            fp = fp.next

        if sp.next:
            # sp.val = sp.next.val
            sp.next = sp.next.next
        head = head.next
        return head