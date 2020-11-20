# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def rec(root, cmax, cmin):
            if cmax is None:
                cmax, cmin = root.val, root.val
            else:
                # print("1", root.val, cmax, cmin)
                cmax=max(cmax, root.val)
                cmin = min(cmin, root.val)
                
            if not root.left and not root.right:
                return abs(cmax-cmin)
            l,r=0,0
            if root.left:
                l = rec(root.left, cmax, cmin)
            if root.right:
                r=rec(root.right, cmax, cmin)
            # print(root.val, l,r)
            return max(l,r)
        return rec(root, None, None)