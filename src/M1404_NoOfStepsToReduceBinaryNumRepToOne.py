class Solution:
    def numSteps(self, s: str) -> int:

        def convert_to_dec(s):

            i = len(s) - 1
            j = 0
            res = 0
            while i >= 0:
                if s[i] == "1":
                    res += 2 ** j
                j += 1
                i -= 1
            return res

        res = convert_to_dec(s)
        count = 0
        while res > 1:
            if res % 2 == 0:
                res //= 2
            else:
                res += 1
            count += 1

        return count