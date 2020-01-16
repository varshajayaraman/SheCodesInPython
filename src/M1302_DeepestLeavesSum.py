# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        global foundFlag, maxLev, sumVal
        foundFlag = False
        maxLev = -1
        sumVal = 0

        def rec(node, level):
            global foundFlag, maxLev, sumVal
            if not node:
                return
            if not node.left and not node.right:
                if level > maxLev:
                    sumVal = 0
                    sumVal += node.val
                    maxLev = level
                elif level == maxLev:
                    sumVal += node.val

                return
            rec(node.left, level + 1)
            rec(node.right, level + 1)

        rec(root, 0)
        return sumVal




