def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    def fs(node, L, R):
        if not node:
            return 0
        else:
            if node.val >= L and node.val <= R:
                print("node")
                print(node.val)
                x = fs(node.left, L, R) + node.val + fs(node.right, L, R)
                print(x)
            else:
                x = fs(node.left, L, R) + fs(node.right, L, R)
                print(x)

            return x

    summ = 0
    return fs(root, L, R)