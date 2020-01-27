class Solution:
    def longestPalindrome(self, s: str) -> str:
        newS = ""
        for c in s:
            newS += "$" + c
        newS += "$"
        maxC = 0
        beg = 0
        end = 0
        ca = [1 for c in newS]

        ca[0] = 1

        i = 1
        while i < len(newS):
            l = 1
            # print(newS[i-l],newS[i+l], newS[i-l]==newS[i+l])
            while i - l > 0 and i + l < len(newS) and newS[i - l] == newS[i + l]:
                ca[i] += 2
                l += 1

            if ca[i] > maxC:
                # print(ca[i], maxC)
                maxC = ca[i]
                end = i + l
                beg = end - ca[i]
                # print("New: ", beg, end)
            i += 1
        res = "".join(newS[beg:end].split("$"))
        # print(newS, maxC, ca, beg, end, res)
        return res