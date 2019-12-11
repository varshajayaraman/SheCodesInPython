def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    def func(root, sum):
        print(root.val, sum)

        def isLeaf(node):
            if node.left or node.right:
                return False
            else:
                return True

        if sum == 0 and isLeaf(root):
            return True
        else:
            if root.left:
                left = func(root.left, sum - root.left.val)
                if left:
                    return True

            if root.right:
                right = func(root.right, sum - root.right.val)
                if right:
                    return True
            return False

    if not root:
        return False
    print("Initila: ")
    print(sum, root.val)
    return func(root, sum - root.val)