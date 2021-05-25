def findMax(arr):
    maxNo = -1

    for i in arr:
        if i > maxNo:
            maxNo = i
    return maxNo


def findOccurence(arr, ele):
    c = 0
    for i in arr:
        if i == ele:
            c += 1
    return c


def fun(numbers, q):
    res = []
    for e in q:
        j = findMax(numbers[e - 1:])
        k = findOccurence(numbers[e - 1:], j)
        res.append(k)
    print(res)