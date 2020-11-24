# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def rec(oroot, croot, target):
            if oroot==target:
                return croot
            if not oroot:
                return None
            l=rec(oroot.left, croot.left, target)
            r=rec(oroot.right, croot.right, target)
            return l or r
        
        return rec(original, cloned, target)