class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        global res
        res = []

        def rec(low, num, high):
            global res
            addFlag = True
            x = num[0]
            for i in range(1, len(num)):
                if int(x[i - 1]) + 1 > 9:
                    x = num
                    addFlag = False
                    break
                x += str(int(x[i - 1]) + 1)
            num = x
            if low <= int(num) and int(num) <= high and addFlag:
                res.append(int(num))
            if int(num) > high:
                return
            else:
                if num[len(num) - 1] != '9' and addFlag:
                    rec(low, num[1:] + "0", high)
                else:
                    num = "1" + "".join(['0' for i in num])
                    rec(low, num, high)

        if low < 10 and high < 10:
            return res
        rec(low, str(low), high)
        return res