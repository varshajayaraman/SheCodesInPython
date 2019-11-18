# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return 0
            else:
                return 1 + max(height(node.left), height(node.right))

        return height(root)
