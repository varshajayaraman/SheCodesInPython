class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        global visited, hmap
        visited = set([])
        hmap = dict()

        for k in edges:
            if hmap.get(k[0]) is None:
                hmap[k[0]] = []
            if hmap.get(k[1]) is None:
                hmap[k[1]] = []
            hmap[k[0]].append(k[1])
            hmap[k[1]].append(k[0])

        def rec(curr, parent):
            global visited
            visited.add(curr)

            for n in hmap[curr]:
                if n == parent:
                    continue
                if n in visited:
                    print(n, curr, parent, visited)
                    return False
                if rec(n, curr) is False:
                    return False
            return True

        if n == 1:
            return True
        for i in range(n):
            if hmap.get(i) is None:
                return False
        first = rec(0, -1)
        if first is False:
            return False
        for k in hmap.keys():
            if k not in visited:
                return False
        return True