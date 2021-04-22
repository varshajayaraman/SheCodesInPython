class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        global res, nodes
        res = []

        def rec(currNode, path):
            global res
            # print(path, res)

            if currNode == nodes - 1:
                res.append(path + [currNode])
                return
            for n in graph[currNode]:
                rec(n, path + [currNode])

        nodes = len(graph)
        for n in graph[0]:
            rec(n, [0])
        # print(res)
        return res