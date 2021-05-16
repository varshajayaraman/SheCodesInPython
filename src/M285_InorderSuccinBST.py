# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        global found, succ
        found = False
        succ = None

        def leftmost(node):
            if not node.left:
                return node
            return leftmost(node.left)

        def rec(root):
            global found, succ
            if root == p:
                found = True
                return
            if root.left:
                rec(root.left)
            if found and succ is None:
                succ = root
                return
            if succ:
                return
            if root.right:
                rec(root.right)

        if p.right:
            return leftmost(p.right)
        rec(root)
        return succ
