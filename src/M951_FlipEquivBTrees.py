# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def rec(oroot, croot):
            if not oroot and not croot:
                return True
            if not oroot or not croot:
                # print("Here", oroot.val)
                return False
            
            # print(oroot, croot)
            if oroot.val==croot.val:
                x = rec(oroot.left, croot.left) and rec(oroot.right, croot.right)
                y = rec(oroot.left, croot.right) and rec(oroot.right, croot.left)
                print(x or y)
                return x or y
            else:
                return False
                
        return rec(root1, root2)