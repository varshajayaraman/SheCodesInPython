class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        def isSub(a, b):
            i = 0
            j = 0
            while j < len(b) and i < len(a):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(a):
                return True
            return False

        # d.sort(reverse=True)
        # print(d)
        res = ""
        for w in d:
            if isSub(w, s):
                # print(res, w)
                if len(w) > len(res):
                    res = w
                elif len(w) == len(res):
                    res = min(w, res)

        return res