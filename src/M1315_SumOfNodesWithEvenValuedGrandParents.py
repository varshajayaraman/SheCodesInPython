# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        global sumVal
        sumVal = 0

        def rec(node):
            global sumVal
            if not node:
                return
            # print()
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    sumVal += node.left.left.val
                    # print(node.left.left.val)
                if node.left and node.left.right:
                    sumVal += node.left.right.val
                    # print(node.left.right.val)
                if node.right and node.right.left:
                    sumVal += node.right.left.val
                    # print(node.right.left.val)
                if node.right and node.right.right:
                    sumVal += node.right.right.val
                    # print(node.right.right.val)
            rec(node.left)
            rec(node.right)

        rec(root)
        return sumVal