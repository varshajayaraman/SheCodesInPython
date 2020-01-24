def findPrime(n):
    res = [1 for i in range(n + 1)]
    res[0] = 0
    res[1] = 0
    for i in range(2, int(sqrt(n))):
        if res[i] == 1:
            for j in range(i * i, n + 1):
                res[j] = 0
    return res


def findNearest(start, res):
    for i in range(start + 1, 256):
        if res[i] == 1:
            return i


# def findNearestBin(low, high, res, diff):
#     if low<=high:
#         mid = low+int((high-low)/2)
#         if res[mid]==1:
#             diff = min(diff, mid-low)
#         findNearestBin()


def relpaceChar(s):
    res = [1 for i in range(256)]
    res = findPrime(255)
    resS = ""
    for ch in s:
        s = findNearest(ord(ch), res)
        # s = findNearestBin(ord(ch)+1, 255, res, math.inf)
        resS += chr(s)

    return resS