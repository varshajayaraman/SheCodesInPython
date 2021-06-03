# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        global maxSize
        maxSize = 0

        def rec(node):
            global maxSize
            if not node:
                return True, 0, math.inf, -math.inf
            lres, lcount, lmin, lmax = rec(node.left)
            rres, rcount, rmin, rmax = rec(node.right)

            if lres and rres and node.val < rmin and node.val > lmax:
                maxSize = max(maxSize, lcount + rcount + 1)
                return True, lcount + rcount + 1, min(node.val, lmin), max(node.val, rmax)
            else:
                return False, 0, 0, 0

        rec(root)
        return maxSize

