class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        res = ""

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        r = 0

        while n1 >= 0 and n2 >= 0:
            s = ord(num1[n1]) - ord('0') + ord(num2[n2]) - ord('0') + r
            r = s // 10
            s = s % 10
            res = str(s) + res
            n1 -= 1
            n2 -= 1

        while n1 >= 0:
            s = ord(num1[n1]) - ord('0') + r
            r = s // 10
            s = s % 10
            res = str(s) + res
            n1 -= 1

        while n2 >= 0:
            s = ord(num2[n2]) - ord('0') + r
            r = s // 10
            s = s % 10
            res = str(s) + res
            n2 -= 1

        if r > 0:
            res = str(r) + res

        return res