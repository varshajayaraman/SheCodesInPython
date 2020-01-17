"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [(root, 0)]
        currLevel = 0
        res = []
        currList = []
        while len(q) > 0:
            # print(q)
            currEle = q.pop(0)
            currNode = currEle[0]
            level = currEle[1]
            if level == currLevel:
                currList.append(currNode.val)
                for x in currNode.children:
                    q.append((x, level + 1))
            else:
                currLevel = level
                res.append(currList)
                currList = [currNode.val]
                for x in currNode.children:
                    q.append((x, level + 1))

        res.append(currList)
        return res