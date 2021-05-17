# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        global s
        s=0
        def rec(root):
            global s
            if not root:
                return
            if root.left and root.left.left is None and root.left.right is None:
                s+=root.left.val
            rec(root.left)
            rec(root.right)
        rec(root)
        return s