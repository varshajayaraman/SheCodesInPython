"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def DFS(node, parent, visited):
            t = Node(node.val, [])
            visited[node] = t
            for x in node.neighbors:
                if x in visited.keys():
                    t.neighbors.append(visited[x])
                else:
                    DFS(x, t, visited)
                    t.neighbors.append(visited[x])
            return t

        if not node:
            return None
        visited = {}
        # visited.remove(0)
        return DFS(node, None, visited)
