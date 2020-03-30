# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addToHead(self, head, val):
        curr = ListNode(val)
        if not head:
            head = curr
        else:
            curr.next = head
            head = curr
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        t1 = l1
        while t1:
            s1.append(t1.val)
            t1 = t1.next
        t2 = l2
        while t2:
            s2.append(t2.val)
            t2 = t2.next

        head = None
        carry = 0
        while len(s1) > 0 or len(s2) > 0:
            s = 0
            if len(s1) > 0:
                s += s1.pop()
            if len(s2) > 0:
                s += s2.pop()
            s += carry
            carry = s // 10
            s %= 10
            head = self.addToHead(head, s)

        if carry > 0:
            head = self.addToHead(head, carry)
        return head
