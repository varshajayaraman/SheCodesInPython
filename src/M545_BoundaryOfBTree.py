# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        global bound, resl, resr, leaves, maxL
        bound = []
        resl = []
        resr = []
        leaves = []
        maxL = 0
        if not root:
            return bound
        bound.append(root.val)

        def leaf(curr):
            if curr.left is None and curr.right is None:
                return True
            return False

        def getLeftFlag(curr, flag):
            if flag == "left":
                return "left"
            elif flag == "right":
                if curr.right is None:
                    return "right"
                else:
                    return "middle"
            else:
                return "middle"

        def getRightFlag(curr, flag):
            if flag == "left":
                if curr.left is None:
                    return "left"
                else:
                    return "middle"
            elif flag == "right":
                return "right"
            else:
                return "middle"

        def rec(curr, flag):
            if flag == "left":
                resl.append(curr.val)
            elif flag == "right":
                resr.append(curr.val)
            else:
                if leaf(curr):
                    leaves.append(curr.val)
            if curr.left:
                leftChildFlag = getLeftFlag(curr, flag)
                rec(curr.left, leftChildFlag)
            if curr.right:
                rightChildFlag = getRightFlag(curr, flag)
                rec(curr.right, rightChildFlag)

        if root.left:
            rec(root.left, "left")
        if root.right:
            rec(root.right, "right")
        resr.reverse()
        return [root.val] + resl + leaves + resr
