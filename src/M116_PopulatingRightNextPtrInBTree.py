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
            return root
        q = []
        q.append((root, 0))
        while len(q) > 0:

            curr = q.pop(0)
            if len(q) > 0 and curr[1] == q[0][1]:
                curr[0].next = q[0][0]
            else:
                curr[0].next = None

            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
            # print(curr[0].val, curr[0].right)
        return root