# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def rec(root):
            if not root:
                return None
            temp = TreeNode(root.val)
            temp.left = rec(root.right)
            temp.right = rec(root.left)
            return temp

        t = rec(root)
        return t
