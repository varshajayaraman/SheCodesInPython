class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        i = 0
        while i < (len(num)):

            if i + 1 < len(num):
                if num[i] > num[i + 1]:
                    if k > 0:
                        num.pop(i)
                        if i > 1:
                            i -= 2
                        else:
                            i = -1
                        k -= 1
                        # print(num, i)
            i += 1
            # else:
            #     res+=num[i]
            # else:
            #     res+=num[i]

        while k > 0:
            if len(num) > 0:
                num.pop()
                k -= 1
            else:
                break
        # print(num)
        if len(num) == 0:
            return "0"
        else:
            return str(int("".join(num)))