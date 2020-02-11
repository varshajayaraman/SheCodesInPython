# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # print(root.val)
        curr = root
        if not root:
            return None
        right = root.right
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            # print("RIght & Left: ", root.right, root.left)
            root.right = root.left
            root.left = None
            while curr.right:
                curr = curr.right
            curr.right = right

        # print(root)
        return root


