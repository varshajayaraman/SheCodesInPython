# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        q = []
        res = []

        if not root:
            return [0]
        if root.left:
            q.append([root.left, 1])
        if root.right:
            q.append([root.right, 1])
        res.append(root.val)
        prev_l = 1
        currAvg = 0
        currLen = 0
        while len(q) > 0:
            currNode = q.pop(0)
            if currNode[1] != prev_l:
                res.append(currAvg / currLen)
                currAvg = 0
                currLen = 0
                prev_l = currNode[1]
            currAvg += currNode[0].val
            currLen += 1
            if currNode[0].left:
                q.append([currNode[0].left, currNode[1] + 1])
            if currNode[0].right:
                q.append([currNode[0].right, currNode[1] + 1])
            if len(q) == 0:
                res.append(currAvg / currLen)
        return res