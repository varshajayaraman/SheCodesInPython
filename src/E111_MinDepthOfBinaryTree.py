class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append((root, 1))

        while len(queue) > 0:
            tup = queue.pop(0)
            node = tup[0]
            if not node.left and not node.right:
                return tup[1]
            else:
                if node.left:
                    queue.append((node.left, tup[1] + 1))
                if node.right:
                    queue.append((node.right, tup[1] + 1))