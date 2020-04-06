# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return head
        odd = head
        if odd.next is None or odd.next.next is None:
            return head
        even = odd.next

        while even and even.next:
            nextOdd = even.next

            even.next = nextOdd.next
            nextOdd.next = odd.next
            odd.next = nextOdd
            odd = nextOdd
            even = even.next

        return head