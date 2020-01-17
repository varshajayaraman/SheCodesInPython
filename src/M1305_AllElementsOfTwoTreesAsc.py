# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        global res
        res = []

        s1, s2 = [], []
        while root1:
            s1.append(root1)
            root1 = root1.left

        while root2:
            s2.append(root2)
            root2 = root2.left
        while len(s1) > 0 and len(s2) > 0:
            # or root2:

            if s1[len(s1) - 1].val < s2[len(s2) - 1].val:
                currNode = s1.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s1.append(currNode)
                        currNode = currNode.left
            elif s1[len(s1) - 1].val == s2[len(s2) - 1].val:
                # print(s1)
                currNode = s1.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s1.append(currNode)
                        currNode = currNode.left

                currNode = s2.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s2.append(currNode)
                        currNode = currNode.left
            else:
                currNode = s2.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s2.append(currNode)
                        currNode = currNode.left

        if len(s1) > 0:
            while len(s1) > 0:
                currNode = s1.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s1.append(currNode)
                        currNode = currNode.left
        elif len(s2) > 0:
            while len(s2) > 0:
                currNode = s2.pop()
                res.append(currNode.val)
                if currNode.right:
                    currNode = currNode.right
                    while currNode:
                        s2.append(currNode)
                        currNode = currNode.left
        return res