# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        def reverse(start, end):
            t = ListNode(0)
            t.next = start
            head = t
            prev = t
            curr = t.next
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, head.next

        if not head:
            return head

        t = ListNode(0)
        t.next = head
        head = t
        leftPrev = None
        rightPrev = None
        temp = head
        n = 1

        while temp.next:
            if n == left:
                leftPrev = temp
            if n == right:
                rightPrev = temp
                break
            temp = temp.next
            n += 1

        if leftPrev is None or rightPrev is None:
            return head

        rightNext = rightPrev.next.next
        rightPrev.next.next = None
        left, right = reverse(leftPrev.next, rightPrev.next)
        leftPrev.next = left
        right.next = rightNext

        return head.next