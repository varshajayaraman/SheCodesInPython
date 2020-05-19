class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        tot = 0
        maxLen = 0
        st = 0
        for i in range(len(s)):
            tot += abs(ord(s[i]) - ord(t[i]))

            while tot > maxCost:
                tot -= abs(ord(s[st]) - ord(t[st]))
                st += 1
            maxLen = max(maxLen, i - st + 1)
        return maxLen