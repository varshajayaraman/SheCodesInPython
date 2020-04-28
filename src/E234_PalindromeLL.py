# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def rev(head, mid, incl):

            # h=ListNode(None)
            # h.next = head

            prev = None
            curr = head

            if incl:
                while prev is not mid:
                    nex = curr.next
                    curr.next = prev

                    prev = curr
                    curr = nex
                return prev


            else:
                while curr is not mid:
                    nex = curr.next
                    curr.next = prev

                    prev = curr
                    curr = nex
                return prev

        slow = head
        fast = head
        if not head:
            return True

        if not head.next:
            return True

        if not head.next.next:
            if head.val == head.next.val:
                return True
            return False

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next

        if fast.next:
            h1 = rev(head, slow, True)
        else:
            h1 = rev(head, slow, False)

        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        if h1 or h2:
            return False
        return True
