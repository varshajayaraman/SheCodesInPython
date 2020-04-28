class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        hmap = {}
        for x in range(len(S)):
            hmap[S[x]] = x

        maxReach = 0
        st = 0
        res = []
        for i in range(len(S)):
            maxReach = max(hmap[S[i]], maxReach)
            if i == maxReach:
                res.append(i - st + 1)
                st = i + 1

        return res