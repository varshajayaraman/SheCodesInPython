# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global maxL, l
        maxL = 0
        l = 0

        def rec(root):
            global maxL, l

            left = 0
            right = 0
            if root.left:
                left = rec(root.left)
            if root.right:
                right = rec(root.right)

            maxL = max(maxL, left + right)
            l = max(left, right)
            return l + 1

        if not root:
            return 0
        rec(root)
        return maxL