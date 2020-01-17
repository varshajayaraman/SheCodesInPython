# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        global ind
        ind = 1

        def rec(node, parVal, preorder):
            global ind
            if ind == len(preorder):
                return

            if preorder[ind] < node.val:
                # print(node.val, preorder[ind], parVal, "lesser")
                node.left = TreeNode(preorder[ind])
                ind += 1
                rec(node.left, node.val, preorder)

            if ind == len(preorder):
                return

            if preorder[ind] > node.val and preorder[ind] < parVal:
                # print(node.val, preorder[ind], parVal, "greater")
                node.right = TreeNode(preorder[ind])
                ind += 1
                rec(node.right, parVal, preorder)

        root = TreeNode(preorder[0])
        rec(root, math.inf, preorder)
        return root