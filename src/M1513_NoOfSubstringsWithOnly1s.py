def numSub(self, s: str) -> int:
    res = 0
    count = 0
    due = (10 ** 9) + 7

    for i in range(len(s)):
        if s[i] == "0":
            count = 0
        else:
            count += 1
            res = (res + count) % due
        # print(res, count)
    return res