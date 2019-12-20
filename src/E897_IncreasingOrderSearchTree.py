# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def func(root, roo1):

            if root.left:
                temp = func(root.left, roo1)
                x = temp
                while x.right:
                    # print("Climbing")
                    # print(x.val)
                    x = x.right

                x.right = TreeNode(root.val)
                while x.right:
                    # print("Climbing")
                    # print(temp.val)
                    x = x.right
            else:
                temp = TreeNode(root.val)
                x = temp
            print(temp)
            if root.right:
                x.right = func(root.right, roo1)
                # while temp.right:
                #     temp=temp.right
            return temp

        roo1 = TreeNode(0)
        x = func(root, roo1)
        # roo1=roo1.right
        return x