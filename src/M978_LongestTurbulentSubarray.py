def maxTurbulenceSize(self, A: List[int]) -> int:
    maxCount = 0
    count = 1
    gflag = -1
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            maxCount = max(maxCount, count)
            count = 1
        else:
            if A[i] > A[i + 1]:
                if gflag == -1:
                    gflag = 0
                    count += 1
                elif gflag == 1:
                    count += 1
                    gflag = 0
                else:
                    maxCount = max(maxCount, count)
                    count = 2
            else:
                if gflag == -1:
                    gflag = 1
                    count += 1
                elif gflag == 0:
                    count += 1
                    gflag = 1
                else:
                    maxCount = max(maxCount, count)
                    count = 2

        # print(i+1, count, gflag, maxCount)
    maxCount = max(maxCount, count)
    return maxCount