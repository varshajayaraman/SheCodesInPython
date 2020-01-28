class Solution:
    def getNeighbours(self, adjM, node):
        neighbours = []
        for i in range(len(adjM[node])):
            if adjM[node][i] > -1:
                neighbours.append(i)
        return neighbours

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        global count, visited, minN, maxD
        visited = [0 for x in range(n)]
        count = 0
        minN = math.inf
        maxD = -math.inf
        ans = 0
        ansD = 0

        adjM = [[math.inf for x in range(n)] for x in range(n)]

        for e in edges:
            adjM[e[0]][e[1]] = e[2]
            adjM[e[1]][e[0]] = e[2]

        def rec(adjM, curr_node, neigh, distLeft, path, dist, cityList):
            global count, maxD

            for x in neigh:
                if visited[x] == 0:
                    if adjM[curr_node][x] == distLeft:
                        cityList.add(x)
                        maxD = max(maxD, adjM[curr_node][x])
                        count += 1
                        continue
                    elif adjM[curr_node][x] > distLeft:
                        max
                        continue
                    else:
                        cityList.add(x)
                        maxD = max(maxD, dist - (distLeft - adjM[curr_node][x]))
                        visited[x] = 1
                        rec(adjM, x, self.getNeighbours(adjM, x), distLeft - adjM[curr_node][x], path + [x], dist,
                            cityList)
                        visited[x] = 0

        # for i in range((n)):
        #     cityList = {0}
        #     cityList.remove(0)
        #     neigh = self.getNeighbours(adjM, i)
        #     if len(neigh)>0:
        #         visited[i]=1
        #         rec(adjM, i, neigh, distanceThreshold, [i], distanceThreshold, cityList)
        #         visited[i]=0
        #         # print(i, cityList, ansD, maxD)
        #     if len(cityList)<minN:
        #         ans = i
        #         ansD =maxD
        #         minN = len(cityList)
        #     elif len(cityList)==minN:
        #         if maxD>=ansD:
        #             ans=i
        #             ansD=maxD

        def floydWarshall(adjM, n):

            global count, minN, ans
            ans = 0
            ref = [[adjM[i][j] for j in range(n)] for i in range(n)]

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if i == j:
                            continue
                        if ref[i][j] > ref[i][k] + ref[k][j]:
                            ref[i][j] = ref[i][k] + ref[k][j]

            # print(ref)
            for r in range(n):
                for c in range(n):
                    if r == c:
                        continue
                    if ref[r][c] <= distanceThreshold:
                        count += 1
                print(count, minN, ans, r)
                if count <= minN:
                    minN = count
                    ans = r
                count = 0
            #                 print(ans)

            #             print(ans)
            return ans

        return floydWarshall(adjM, n)

        # return ans