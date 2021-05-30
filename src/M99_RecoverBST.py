# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def rec(curr):
            global pred, x, y
            if not curr:
                return

            rec(curr.left)
            if pred and curr.val < pred.val:
                y = curr
                if x is None:
                    x = pred
                else:
                    return
            pred = curr
            rec(curr.right)

        global pred, x, y
        pred = None
        x, y = None, None
        rec(root)
        # print(a.val,b.val)
        # if a is not None and b is not None:
        t = x.val
        x.val = y.val
        y.val = t
