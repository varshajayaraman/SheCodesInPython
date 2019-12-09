def inorderTraversal(self, root: TreeNode) -> List[int]:
    def ir(node, res):
        if node:
            ir(node.left, res)
            res.append(node.val)
            ir(node.right, res)

    res = []
    ir(root, res)
    return res