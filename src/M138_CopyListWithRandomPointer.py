"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping = {}
        if head == None:
            return None
        t = head
        t1 = Node(t.val, None, None)
        mapping[t] = t1
        tnew = t1

        while (t.next):
            if t.next in mapping.keys():
                t1.next = mapping[t.next]
            else:
                t1.next = Node(t.next.val, None, None)
                mapping[t.next] = t1.next
            if t.random == None:
                t1.random = None
            else:
                if t.random in mapping.keys():
                    t1.random = mapping[t.random]

                else:
                    t1.random = Node(t.random.val, None, None)
                    mapping[t.random] = t1.random
            t = t.next
            t1 = t1.next
        if t.random == None:
            t1.random = None
        else:
            if t.random in mapping.keys():
                t1.random = mapping[t.random]

            # else:
            #     t1.random =  Node(t.random.val,t.random.next,t.random.random)
            #     mapping[t.random]=t1.random
        return tnew
