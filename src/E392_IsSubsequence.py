class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0

        while i < len(t):
            if j == len(s):
                return True
            if s[j] == t[i]:
                i += 1
                j += 1
            else:
                i += 1

        if j == len(s):
            return True
        return False