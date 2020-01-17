"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        global res
        res = []

        def rec(node):
            if not node:
                return
            res.append(node.val)
            for i in node.children:
                rec(i)

        def itera(root):
            if not root:
                return
            s = [root]

            while len(s) > 0:
                currNode = s.pop()
                # print(currNode)
                res.append(currNode.val)

                for c in range(len(currNode.children) - 1, -1, -1):
                    s.append(currNode.children[c])

                    # rec(root)

        itera(root)
        return res