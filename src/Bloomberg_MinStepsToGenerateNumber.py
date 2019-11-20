import math
class node:
    def __init__(self,val,level):
        self.val=val
        self.level=level


def solution(n):

    def rec(n,queue):
        while len(queue)>0:
            curr = queue.pop(0)
            visited.append(curr.val)
            if curr.val == n:
                return curr.level
            else:
                if curr.val*2==n or int(curr.val/3)==n:
                    return curr.level+1
                else:
                    if curr.val*2 not in visited:
                        queue.append(node(curr.val*2, curr.level+1))

                    if int(curr.val/3) not in visited:
                        queue.append(node(curr.val/3, curr.level + 1))

        return
    queue=[node(1,0)]
    visited = []
    print(rec(n,queue))
