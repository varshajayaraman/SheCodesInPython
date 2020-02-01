# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseLL(self, head):
        prev, curr, after_curr = head, head.next, False
        while curr:
            after_curr = curr.next
            curr.next = prev
            if prev == head:
                head.next = None
            prev = curr
            curr = after_curr
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        temp, head = None, None
        carry = 0
        # l1=self.reverseLL(l1)
        # l2=self.reverseLL(l2)
        while l1 or l2:
            if l1 and l2:
                sumVal = l1.val + l2.val + carry
                carry = sumVal // 10
                sumVal = sumVal % 10
                if not head:
                    head = ListNode(sumVal)
                    temp = head
                else:
                    head.next = ListNode(sumVal)
                    head = head.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sumVal = l1.val + carry
                carry = sumVal // 10
                sumVal = sumVal % 10
                if not head:
                    head = ListNode(sumVal)
                    temp = head
                else:
                    head.next = ListNode(sumVal)
                    head = head.next
                l1 = l1.next
            else:
                sumVal = l2.val + carry
                carry = sumVal // 10
                sumVal = sumVal % 10
                if not head:
                    head = ListNode(sumVal)
                    temp = head
                else:
                    head.next = ListNode(sumVal)
                    head = head.next
                l2 = l2.next
            print(head)
        if carry > 0:
            head.next = ListNode(carry)
            print(head)
            head = head.next
        print("After carry: ", temp)
        #         while l1:
        #             # print(s1)
        #             s1.append(l1.val)
        #             l1=l1.next
        #         while l2:
        #             # pr
        #             s2.append(l2.val)
        #             l2=l2.next

        #         while len(s1)>0 or len(s2)>0:
        #             if len(s1)>0 and len(s2)>0:
        #                 sumVal = s1.pop(-1)+s2.pop(-1)+carry
        #                 carry = sumVal//10
        #                 sumVal = sumVal%10
        #                 if not head:
        #                     head = ListNode(sumVal)
        #                 else:
        #                     temp = ListNode(sumVal)
        #                     temp.next = head
        #                     head=temp
        #             elif len(s1)>0:
        #                 sumVal = s1.pop(-1)+carry
        #                 carry = sumVal//10
        #                 sumVal = sumVal%10
        #                 if not head:
        #                     head = ListNode(sumVal)
        #                 else:
        #                     temp = ListNode(sumVal)
        #                     temp.next = head
        #                     head=temp
        #             else:
        #                 sumVal = s2.pop(-1)+carry
        #                 carry = sumVal//10
        #                 sumVal = sumVal%10
        #                 if not head:
        #                     head = ListNode(sumVal)
        #                 else:
        #                     temp = ListNode(sumVal)
        #                     temp.next = head
        #                     head=temp
        #         if carry>0:
        #             temp = ListNode(carry)
        #             temp.next=head
        #             head=temp
        # head = self.reverseLL(temp)
        return temp
