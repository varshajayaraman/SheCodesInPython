# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:

        temp = root
        if not root:
            root = TreeNode(val)

        if root.val < val:
            curr = TreeNode(val)
            curr.left = root
            root = curr

        else:  # Node is greater than val
            while temp.right and temp.right.val > val:
                temp = temp.right
            if not temp.right:
                temp.right = TreeNode(val)
            else:
                curr = TreeNode(val)
                curr.left = temp.right
                temp.right = curr
        return root

