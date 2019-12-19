class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        final = []
        inter = []
        queue = []
        if not root:
            return final
        queue.append((root, 1))
        while len(queue) > 0:
            tup = queue.pop(0)
            inter.append(tup[0].val)
            node = tup[0]
            if node.left:
                queue.append((node.left, tup[1] + 1))
            if node.right:
                queue.append((node.right, tup[1] + 1))
            if len(queue) > 0:
                if tup[1] != queue[0][1]:
                    final.append(inter)
                    inter = []
            if len(queue) == 0:
                final.append(inter)
                inter = []
            # print(queue)

        return final