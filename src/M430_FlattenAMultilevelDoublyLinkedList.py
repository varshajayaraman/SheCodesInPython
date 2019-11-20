"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def p(t1):
            h = t1
            print("At this point: ")
            while h:
                print((h.val))
                h = h.next

        def soln(t):

            if t:
                print(t.val)
                t1 = Node(t.val, None, None, None)
                temp = t1
                if t.child is not None:
                    temp.next = soln(t.child)
                    temp.next.prev = temp
                    print("Looped from " + str(t1.val))
                    while temp.next:
                        temp = temp.next
                    print("Looped to " + str(t1.val))
                if t.next:
                    temp.next = soln(t.next)
                    temp.next.prev = temp
                    #
                p(t1)
                return t1

        t = head
        t1 = soln(t)
        print("break")
        x = t1
        while t1:
            print(t1.val)
            t1 = t1.next
        return x