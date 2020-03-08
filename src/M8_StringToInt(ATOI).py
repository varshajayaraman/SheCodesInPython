class Solution:
    def myAtoi(self, str: str) -> int:
        num = None
        i = 0
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)
        sign = None
        while i < len(str):
            if str[i] == '.':
                break
            if str[i] == '+':
                if not num:
                    if sign is None:
                        sign = 1
                    else:
                        return 0
                else:
                    break

            if str[i] == '-':
                if not num:
                    print(sign)
                    if sign is None:
                        sign = -1
                    else:
                        return 0
                else:
                    break
            if str[i].isalpha():
                break
            if str[i].isdigit():
                if sign is None:
                    sign = 1
                curr = ord(str[i]) - ord('0')
                if num is None:
                    num = 0
                if sign > 0 and INT_MAX - (num * 10) < curr:
                    return INT_MAX
                elif sign < 0 and INT_MIN + (num * 10) > -curr:
                    return INT_MIN
                num = (num * 10) + curr
            elif str[i] == " ":
                print(num, sign)
                if num or sign:
                    break
            i += 1
        if sign == -1 and num:
            num = -num
        if not num:
            return 0
        return num


