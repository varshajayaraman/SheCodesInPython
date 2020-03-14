# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.c1 = None
        self.c2 = None
        self.anc = None

    def reset(self):
        self.c1 = None
        self.c2 = None
        self.anc = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.reset()
        self.lca(root, p, q)
        return self.anc

    def lca(self, root, p, q):
        if not root:
            return 0

        l, r, c = 0, 0, 0
        if root.val == p.val or root.val == q.val:
            c = 1

        l = self.lca(root.left, p, q)

        r = self.lca(root.right, p, q)
        if l + r + c == 2:
            if not self.anc:
                self.anc = root
        #     else:
        #         return 1
        # else:
        return max(l, r, c)


