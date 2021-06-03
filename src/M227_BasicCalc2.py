class Solution:
    def calculate(self, s: str) -> int:
        lastNum = 0
        currNum = 0
        op = "+"
        res = 0

        for i in range(len(s)):
            if s[i].isdigit():
                currNum = (currNum * 10) + int(s[i])
            elif s[i] == " ":
                continue
            else:
                if op == "+":
                    res += lastNum
                    lastNum = currNum
                elif op == "-":
                    res += lastNum
                    lastNum = currNum * -1
                elif op == "*":
                    lastNum = lastNum * currNum
                else:
                    lastNum = int(lastNum / currNum)
                op = s[i]
                currNum = 0
        if op == "+":
            res += (lastNum + currNum)
        elif op == "-":
            res += (lastNum - currNum)
        elif op == "*":
            res += lastNum * currNum
        else:
            print(lastNum, currNum, (lastNum / currNum))
            res += int(lastNum / currNum)
        return res