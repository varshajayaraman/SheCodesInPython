class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}

        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] = -1
            else:
                hmap[s[i]] = i
        for ch in s:
            if hmap[ch] > -1:
                return hmap[ch]
        return -1