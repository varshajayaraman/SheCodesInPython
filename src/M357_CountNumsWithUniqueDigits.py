class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        global count
        count = 0
        ref = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        def dp():
            res = [0 for i in range(n + 1)]
            res[0] = 1
            res[1] = 9
            # res[2]=81
            for i in range(2, n + 1):
                res[i] = res[i - 1] * (10 - i + 1)

            s = 0
            for i in range(n + 1):
                s += res[i]
            return s

        def rec(currNum, ref):
            global count
            # print(currNum)

            if currNum < (pow(10, n)):
                count += 1

            for i in range(len(ref)):
                if ref[i] >= 0:
                    new_currNum = (currNum * 10) + ref[i]
                    if new_currNum > pow(10, n):
                        continue
                    ref[i] = -1
                    rec(new_currNum, ref)
                    ref[i] = i

        for i in range(1, len(ref)):
            ref[i] = -1
            rec(i, ref)
            ref[i] = i
        # return dp()
        # rec()
        return count + 1
