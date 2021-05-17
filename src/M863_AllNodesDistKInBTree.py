# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        global res
        res = []

        def subtree(root, l):
            if not root:
                return
            global res
            if l == k:
                res.append(root.val)
                return
            subtree(root.left, l + 1)
            subtree(root.right, l + 1)

        def rec(root):
            global res
            if not root:
                return -1
            if root == target:
                if k == 0:
                    res.append(root.val)
                subtree(root.left, 1)
                subtree(root.right, 1)
                return 1
            l = rec(root.left)
            r = rec(root.right)
            if l == -1 and r == -1:
                return -1
            if l != -1:
                if l == k:
                    res.append(root.val)
                subtree(root.right, l + 1)
                return l + 1
            elif r != -1:
                if r == k:
                    res.append(root.val)
                subtree(root.left, r + 1)
                return r + 1

        rec(root)
        return res