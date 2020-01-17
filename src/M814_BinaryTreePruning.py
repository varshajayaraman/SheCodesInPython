# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        left, right = None, None
        if root.left:
            left = self.pruneTree(root.left)
            if not left:
                root.left = None
        if root.right:
            right = self.pruneTree(root.right)
            if not right:
                root.right = None
        if root.val == 1 or left or right:
            return root
        else:
            return None


