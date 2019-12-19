# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        final=[]
        inter=[]
        queue=[]
        straight=True
        if not root:
            return final
        queue.append((root,1))
        while len(queue)>0:
            tup = queue.pop(0)
            inter.append(tup[0].val)
            node = tup[0]
            if node.left:
                queue.append((node.left, tup[1] + 1))
            if node.right:
                queue.append((node.right, tup[1] + 1))
            if len(queue) > 0:
                if tup[1] != queue[0][1]:
                    if straight==True:
                        final.append(inter)
                        straight=False
                    else:
                        print(inter)
                        print(inter[::-1])
                        rev=inter[::-1]
                        final.append(rev)
                        straight=True
                    inter = []
            if len(queue) == 0:
                if straight==True:
                    final.append(inter)
                else:
                    rev=inter[::-1]
                    final.append(rev)
                inter = []
            # print(queue)

        return final