# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtreeUtil(self, s, t):
        left, right = True, True

        if s.left and t.left:
            if s.left.val == t.left.val:
                left = self.isSubtreeUtil(s.left, t.left)
            else:
                return False
        else:
            if s.left or t.left:
                return False

        if s.right and t.right:
            if s.right.val == t.right.val:
                right = self.isSubtreeUtil(s.right, t.right)
            else:
                return False
        else:
            if s.right or t.right:
                return False
        return left and right

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        left, right = True, True
        if s and t:
            print
            if s.val == t.val:
                if self.isSubtreeUtil(s, t):
                    return True

            if not s.left and not s.right:
                return False
            if s.left:
                left = self.isSubtree(s.left, t)
                if left:
                    return True
            if s.right:
                right = self.isSubtree(s.right, t)
                if right:
                    return True
                else:
                    return False
        elif not s and not t:
            return True
        else:
            return False