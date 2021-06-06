class Solution:
    def countSubstrings(self, s: str) -> int:
        def countsub(s, start, end):
            l = 0
            while 0 <= start < len(s) and start <= end < len(s) and s[start] == s[end]:
                l += 1
                start -= 1
                end += 1
            return l

        ans = 0

        for i in range(len(s)):
            ans += countsub(s, i, i)
            ans += countsub(s, i, i + 1)
        return ans

