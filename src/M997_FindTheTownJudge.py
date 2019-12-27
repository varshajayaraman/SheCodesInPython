class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        def allTrust(adj, r):
            for x in range(len(adj)):
                if x == r:
                    continue
                if adj[x][r] != 1:
                    return False
            return True

        adj = [[0 for x in range(N)] for x in range(N)]
        # print(adj)
        for i in trust:
            adj[i[0] - 1][i[1] - 1] = 1
        # print(adj)

        for r in range(N):
            # print(adj[r])
            if 1 not in adj[r] and allTrust(adj, r):
                return r + 1
        return -1
