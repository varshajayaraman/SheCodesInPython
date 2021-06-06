# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head
        t = ListNode(0)
        t.next = head
        head = t

        prev = t
        curr = head.next
        delFlag = False
        while curr:
            nxt = curr.next
            if nxt is None:
                break
            if curr.val == nxt.val:
                curr.next = nxt.next
                delFlag = True
            else:
                if delFlag is True:
                    prev.next = nxt
                    delFlag = False

                else:
                    prev = prev.next
                curr = prev.next
        if delFlag is True:
            prev.next = None
        return head.next