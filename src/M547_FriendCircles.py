class Solution:
    def dfs(self, M, curr_i):
        for n in range(len(M[curr_i])):
            if M[curr_i][n] == 1:
                M[curr_i][n] = -1
                self.dfs(M, n)

    def findCircleNum(self, M: List[List[int]]) -> int:
        global count
        count = 0
        for i in range(len(M)):
            if 1 in M[i]:
                # fs = set([0])
                M[i][i] = -1
                self.dfs(M, i)
                count += 1
        return count
