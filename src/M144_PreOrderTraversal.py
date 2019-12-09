def preorderTraversal(self, root: TreeNode) -> List[int]:
    def pr(node, res):
        if not node:
            return
        else:
            res.append(node.val)
            pr(node.left, res)
            pr(node.right, res)


    res = []
    pr(root, res)
    return res