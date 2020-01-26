def paintWays(arr):
    start=-1
    end=-1
    prevOne=-1
    totCount = 1
    zCount = 1

    for i in range(len(arr)):
        if arr[i]==0:
            if prevOne >-1:
                zCount +=1
            else:
                start +=1
        elif arr[i] == 1:
            if prevOne == -1:
                prevOne = i
            else:
                totCount *= (zCount)
                zCount = 1
                prevOne = i
    if zCount > 0:
        end = zCount
        zCount = 0

    if prevOne == -1:
        return 0
    else:
        return totCount