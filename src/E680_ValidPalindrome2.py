class Solution:
    def validPalindrome(self, s: str) -> bool:

        def rec(start, end, oneFlag=False):
            if start >= end:
                return True
            if s[start] == s[end]:
                return rec(start + 1, end - 1, oneFlag)
            else:
                if oneFlag is True:
                    return False
                return rec(start, end - 1, True) or rec(start + 1, end, True)

        if len(s) == 1:
            return True
        return rec(0, len(s) - 1)