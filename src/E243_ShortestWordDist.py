class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        w1 = None
        w2 = None
        minD = math.inf
        wd = wordsDict
        for i in range(len(wd)):
            # print(wd[i],w1)
            if wd[i] == word1:
                if w1 is not None and w2 is not None:
                    minD = min(minD, abs(w2 - w1))
                w1 = i
            if wd[i] == word2:
                if w1 is not None and w2 is not None:
                    minD = min(minD, abs(w2 - w1))
                w2 = i
        if w1 is not None and w2 is not None:
            minD = min(minD, abs(w2 - w1))
        return minD