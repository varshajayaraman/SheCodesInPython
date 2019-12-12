# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = 0

        def fu(root):
            global res
            if not root:
                return
            fu(root.right)
            self.res = self.res + root.val
            root.val = self.res
            fu(root.left)

        fu(root)
        return root