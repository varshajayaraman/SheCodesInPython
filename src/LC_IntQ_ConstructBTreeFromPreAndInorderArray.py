# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        global hmap, rind
        rind = 0
        hmap = {}
        for j in range(len(inorder)):
            hmap[inorder[j]] = j
        print(hmap)

        def rec(preorder, inorder, l, h):
            if l > h:
                return
            global rind

            root = TreeNode(preorder[rind])
            ind = hmap[preorder[rind]]

            # print(ind, l, h)

            if l < ind:
                rind += 1
                # print("Going left for node: "+str(root.val)+" with rind: "+str(rind)+" l,h: "+str(l)+", "+str(ind-1))
                root.left = rec(preorder, inorder, l, ind - 1)

            if ind + 1 <= h:
                rind += 1
                # print("Going right for node: "+str(root.val)+" with rind: "+str(rind)+" l,h: "+str(ind+1)+", "+str(h))
                root.right = rec(preorder, inorder, ind + 1, h)

            return root

        return rec(preorder, inorder, 0, len(inorder) - 1)