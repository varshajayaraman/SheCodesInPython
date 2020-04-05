# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        global count, tar
        count = 0
        tar = 0

        def rec(root, k):

            global count, tar
            if count > k:
                return

            if root.left:
                rec(root.left, k)
            count += 1
            if count == k:
                # print("Setting:", root.val, count)
                tar = root.val
                return
            if root.right:
                rec(root.right, k)

        if not root:
            return tar
        rec(root, k)
        return tar