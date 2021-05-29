class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def getmap(pre):
            hmap = dict()
            for p in pre:
                if hmap.get(p[0]) is None:
                    hmap[p[0]] = [p[1]]
                else:
                    hmap[p[0]].append(p[1])
            return hmap

        def dfs(currPath):
            global visited, path, cycleFlag

            currCourse = currPath[-1]
            if hmap.get(currCourse) is None:
                return
            choices = hmap[currCourse]

            for c in choices:
                if c in visited:
                    cycleFlag = True
                    return
                visited.add(c)
                dfs(currPath + [c])
                visited.remove(c)
                path.append(c)
                if cycleFlag:
                    return

        global hmap, visited, path, cycleFlag
        visited = set([numCourses - 1])
        globalPath = []
        cycleFlag = False
        hmap = getmap(prerequisites)
        gbDict = set()
        for i in range(0, numCourses):
            if i not in gbDict:
                cycleFlag = False
                path = []
                visited = set([i])
                dfs([i])
                if cycleFlag is True:
                    return []
                path.append(i)
                for j in path:
                    if j not in gbDict:
                        globalPath.append(j)
                        gbDict.add(j)

        return globalPath