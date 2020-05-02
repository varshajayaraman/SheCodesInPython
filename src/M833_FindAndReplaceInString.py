class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        j = 0
        i = 0
        h = {}
        for i in range(len(indexes)):
            h[indexes[i]] = [sources[i], targets[i]]
        res = []
        i = 0
        while i < (len(S)):

            if h.get(i) is not None:
                src = h[i][0]
                tar = h[i][1]
                if S[i:i + len(src)] == src:
                    # print(i, j, indexes[j], sources[j], targets[j])
                    res.append(tar)
                    i += len(src)
                else:
                    res.append(S[i])
                    i += 1
            else:
                res.append(S[i])
                i += 1
            # print(res)

        return "".join(res)
