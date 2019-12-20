# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    delete = False
    res = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        def delNode(root, to_delete):
            if root.left:
                delNode(root.left, to_delete)
                if self.delete:
                    root.left = None
                    self.delete = False

            if root.right:
                delNode(root.right, to_delete)
                if self.delete:
                    root.right = None
                    self.delete = False
            if root.val in to_delete:
                if root.left:
                    self.res.append(root.left)
                if root.right:
                    self.res.append(root.right)
                print(root.val)
                root.left = None
                root.right = None
                root = None
                self.delete = True
            else:
                self.delete = False

            return self.res

        x = delNode(root, to_delete)
        self.res = []
        if not self.delete:
            x.append(root)
        return x
