# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        global sumVal
        sumVal = 0
        
        def rec(root):
            global sumVal
            
            if not root:
                return
            if root.val>=low and root.val<=high:
                sumVal += root.val
            
            rec(root.left)
            rec(root.right)
            
        rec(root)
        return sumVal