class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        def anagram(sdict, pdict):
            for k, v in pdict.items():
                if k not in sdict or sdict[k] != v:
                    return False
            return True

        pMap, sMap = {}, {}
        res = []

        for c in p:
            if c in pMap:
                pMap[c] += 1
            else:
                pMap[c] = 1

        if len(s) < len(p):
            return res

        st = 0
        l = st + len(p) - 1
        for i in range(len(p) - 1):
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1

        while l < len(s):
            if s[l] in sMap:
                sMap[s[l]] += 1
            else:
                sMap[s[l]] = 1
            if anagram(sMap, pMap):
                res.append(st)
            sMap[s[st]] -= 1
            st += 1
            l += 1

        return res
