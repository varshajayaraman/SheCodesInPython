class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def getEnd(s, st):
            i = st
            while i < len(s) and s[i] != ' ':
                i += 1
            return i - 1

        i = 0
        l = len(s) - 1
        while i < l:
            t = s[i]
            s[i] = s[l]
            s[l] = t
            i += 1
            l -= 1
        # return s

        i = 0
        while i < len(s):
            e = getEnd(s, i)
            l = e
            while i < e:
                t = s[i]
                s[i] = s[e]
                s[e] = t
                i += 1
                e -= 1
            i = l + 2
        return s