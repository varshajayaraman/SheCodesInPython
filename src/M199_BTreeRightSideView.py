# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        global res, maxLevel
        res = []
        maxLevel = -math.inf

        def rec(root, level):
            global res, maxLevel
            if not root:
                return
            if level > maxLevel:
                maxLevel = level
                res.append(root.val)
            if root.right:
                rec(root.right, level + 1)
            if root.left:
                rec(root.left, level + 1)
            return

        rec(root, 0)
        return res