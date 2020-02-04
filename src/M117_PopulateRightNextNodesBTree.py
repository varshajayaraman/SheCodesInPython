"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return
        q = [(root, 1)]
        while len(q) > 0:
            curr = q.pop(0)
            if len(q) == 0:
                curr[0].next = None
            else:
                if q[0][1] == curr[1]:
                    curr[0].next = q[0][0]
            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
        #         if not root:
        #             return
        #         print(root.val)
        #         if root.left:
        #             print("Left: ", root.val, root.left is None)
        #             if root.right:
        #                 root.left.next = root.right
        #             elif root.next:
        #                 t=root
        #                 while t.next:
        #                     if t.next.left:
        #                         root.left.next = t.next.left
        #                         break
        #                     elif t.next.right:
        #                         root.left.next = t.next.right
        #                         break
        #                     else:
        #                         t=t.next

        #         if root.right:
        #             if root.next:
        #                 t=root
        #                 while t.next:
        #                     # print(t.val, t.next.val, t.next.left, t.next.right, t.next.next)
        #                     if t.next.left:
        #                         root.right.next = t.next.left
        #                         break
        #                     elif t.next.right:
        #                         root.right.next = t.next.right
        #                         break
        #                     else:
        #                         t=t.next

        #         self.connect(root.left)
        #         self.connect(root.right)

        return root