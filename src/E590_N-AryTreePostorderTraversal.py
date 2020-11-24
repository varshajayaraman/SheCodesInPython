"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        
        while len(stack)>0:
            
            curr=stack[-1]
            stack.pop(len(stack)-1)
            res.append(curr.val)
            # print(curr, res)
            stack.extend(curr.children)
            
        res.reverse()
        return res