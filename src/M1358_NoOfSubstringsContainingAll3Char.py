class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        res = 0
        i = 0

        j = 0
        count = 0
        h = {}
        h['a'] = 0
        h['b'] = 0
        h['c'] = 0
        while j < len(s):
            h[s[j]] += 1

            while all(x > 0 for x in h.values()):
                h[s[i]] -= 1
                i += 1
                count += 1
            res += count
            j += 1

        # print(h, res, /c)
        while all(x > 0 for x in h.values()):
            h[s[i]] -= 1
            i += 1
            count += 1
        return res