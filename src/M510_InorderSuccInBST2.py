"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        global succ, pred
        succ = None
        pred = None

        def getLeftMost(root):

            while root.left:
                root = root.left
            return root

        def getSmallest(root):
            node = root
            while root.parent and root.parent.val < node.val:
                # print(root.)
                root = root.parent
            return root.parent

        if node.right:
            return getLeftMost(node.right)
        else:
            return getSmallest(node)

