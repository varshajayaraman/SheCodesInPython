class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        def f1():
            s = list(s)
            minCost = 0
            i = 0
            n = 0
            while i < len(s):
                if s[i] == -1:
                    i += 1
                    continue
                if i == n:
                    n += 1
                if n >= len(s):
                    break
                # print(i,n)
                if s[i] == s[n]:
                    minCost += min(cost[i], cost[n])
                    if cost[i] <= cost[n]:
                        s[i] = -1
                        i += 1
                    else:
                        s[n] = -1
                        n += 1
                else:
                    i += 1
                    n += 1

            return minCost

        def f2(s, cost):
            s = list(s)
            minCost = 0

            def getSame(s, i):
                for j in range(i, len(s)):
                    if s[i] != s[j]:
                        return j - 1
                return j

            i = 0
            while i < len(s) - 1:
                j = getSame(s, i)
                if j == i:
                    i += 1
                    continue
                sumCost = sum(cost[i:j + 1])
                maxCost = max(cost[i:j + 1])
                minCost += (sumCost - maxCost)
                i = j + 1
            return minCost

        return f2(s, cost)