def numDecodings(s):
    res = [1]
    if s[0] == '0':
        res.append(0)
    else:
        res.append(1)
    for i in range(1, len(s)):
        sum = 0
        if int(s[i]) > 0:
            sum += res[len(res) - 1]
        if int(s[i - 1]) * 10 + int(s[i]) >= 10 and int(s[i - 1]) * 10 + int(s[i]) <= 26:
            sum += res[len(res) - 2]

        res.append(sum)
    return res[len(res) - 1]