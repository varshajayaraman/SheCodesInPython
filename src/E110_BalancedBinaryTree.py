# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def heightDiff(node):
            if not node:
                return 0
            else:
                l = heightDiff(node.left)
                r = heightDiff(node.right)
                print(l, r)
                if abs(l - r) > 1 or l == -1 or r == -1:
                    return -1
                else:
                    return max(l, r) + 1

        if heightDiff(root) == -1:
            return False
        else:
            return True
