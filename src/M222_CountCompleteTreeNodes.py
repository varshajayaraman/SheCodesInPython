# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        global leafCount, maxLev
        maxLev = -1
        leafCount = 0

        def rec(node, lev):
            global maxLev, leafCount
            maxLev = max(maxLev, lev)
            if node.left is None and node.right is None and lev == maxLev:
                # print(node.val)
                leafCount += 1

            if node.left:
                rec(node.left, lev + 1)
            if node.right:
                rec(node.right, lev + 1)

        if not root:
            return 0
        rec(root, 0)
        print(leafCount, maxLev)
        return leafCount + pow(2, maxLev) - 1
