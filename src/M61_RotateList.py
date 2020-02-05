# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        i = 0
        c = 0
        t = head
        while t:
            c += 1
            t = t.next
        if k == 0 or c == 0:
            return head
        k = k % c

        if not head:
            return head
        fast = head
        while i < k:
            if fast.next:
                fast = fast.next
            else:
                fast = head
            i += 1
        slow = head

        while fast.next:
            slow = slow.next
            fast = fast.next

        if not slow.next:
            return head
        nh = slow.next
        slow.next = None
        fast.next = head
        head = nh

        return head