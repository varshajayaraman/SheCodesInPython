# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSmallest(self, tar):
        succ = None

        if tar.right.left:
            t = tar.right
            while t.left.left:
                t = t.left
            succ = t.left
            # print(t.val)
            if succ.right:
                t.left = succ.right
            else:
                t.left = None
            return succ
        else:
            succ = tar.right
            tar.right = succ.right
            return succ

    def findParent(self, temp, key):
        if not temp:
            return None
        # print(temp, key)
        if temp.val == 'A':
            if temp.right.val == key:
                return temp
            return self.findParent(temp.right, key)

        if (temp.right and temp.right.val == key) or (temp.left and temp.left.val == key):
            return temp

        if temp.val < key:
            return self.findParent(temp.right, key)
        else:
            return self.findParent(temp.left, key)
        return None

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        t = TreeNode('A')
        t.right = root
        root = t

        p = self.findParent(t, key)
        # print(p)
        if not p:
            return root.right
        if p.left and p.left.val == key:
            if p.left and p.left.right:
                succ = self.findSmallest(p.left)
                succ.left = p.left.left
                succ.right = p.left.right
                p.left = succ
            else:
                p.left = p.left.left
            # return t
        else:
            if p.right and p.right.right:
                succ = self.findSmallest(p.right)
                succ.left = p.right.left
                succ.right = p.right.right
                p.right = succ
            else:
                p.right = p.right.left
            # return t
        return root.right






