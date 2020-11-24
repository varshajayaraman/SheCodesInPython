# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global num
        num=0
        def rec(root, maxV):
            global num
            if root.val>=maxV:
                num +=1
                maxV = root.val
            if root.left:
                rec(root.left, maxV)
            if root.right:
                rec(root.right, maxV)
                
        rec(root, root.val)
        return num