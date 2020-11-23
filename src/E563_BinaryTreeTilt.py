# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        global sumV
        sumV=0
        def rec(root):
            global sumV
            if not root:
                return 0
            
            left_new, right_new = None, None
            left_new = rec(root.left)
            right_new = rec(root.right)
            
            sumV += abs(left_new-right_new)
            # root_new.left = left_new[1]
            # root_new.right = right_new[1]
            return root.val+ left_new+right_new
        
        rec(root)
        return sumV