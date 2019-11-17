"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        nodes=[]
        if not root:
            return 0
        count=1
        nodes.append((root,1))
        currCount=1
        while len(nodes)>0:
            currItem = nodes.pop(0)
            currNode = currItem[0]
            currCount = currItem[1]
            for x in currNode.children:
                nodes.append((x,currCount+1))
        return currCount