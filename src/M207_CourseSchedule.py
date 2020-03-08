class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        global adjDict, visited
        adjDict = {}
        for r in prerequisites:
            if r[0] in adjDict:
                adjDict[r[0]].append(r[1])
            else:
                adjDict[r[0]] = [r[1]]

        print(adjDict)

        def dfs(c):
            global visited
            if c not in adjDict:
                return True
            elif adjDict[c][0] in visited:
                return False
            else:
                for p in adjDict[c]:
                    visited.add(p)
                    if not dfs(p):
                        return False
                    visited.remove(p)
                return True

        global visited

        for c in range(numCourses):
            visited = set()
            visited.add(c)
            if not dfs(c):
                return False

        return True
