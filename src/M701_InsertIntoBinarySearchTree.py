# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        k = root
        while (1):
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    break
            elif root.val > val:
                if root.left:
                    root = root.left
                else:
                    break
            else:
                break
        if val < root.val:
            root.left = TreeNode(val)
        else:
            root.right = TreeNode(val)

        return k