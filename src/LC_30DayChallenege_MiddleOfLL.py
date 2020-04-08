# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        slow = head
        fast = head.next.next

        while fast.next and fast.next.next:
            # print(slow.val)
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)
        if not fast.next:
            return slow.next
        return slow.next.next