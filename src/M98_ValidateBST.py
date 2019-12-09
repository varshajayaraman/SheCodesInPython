def isValidBST(self, root: TreeNode) -> bool:
    def isv(node, maxv, minv):
        if node.val < maxv and node.val > minv:
            if node.left and not node.right:
                return isv(node.left, node.val, minv)
            elif not node.left and node.right:
                return isv(node.right, maxv, node.val)
            elif not node.left and not node.right:
                return True
            else:
                return isv(node.left, node.val, minv) and isv(node.right, maxv, node.val)
        else:
            return False

    if not root:
        return True
    else:
        if root.left and not root.right:
            return isv(root.left, root.val, -math.inf)
        elif not root.left and root.right:
            return isv(root.right, math.inf, root.val)
        elif not root.left and not root.right:
            return True
        else:
            return isv(root.left, root.val, -math.inf) and isv(root.right, math.inf, root.val)