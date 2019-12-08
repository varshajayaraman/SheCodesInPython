def longestOnes(self, A: List[int], K: int) -> int:
    def findzero(A, last, i):
        for x in range(last + 1, i):
            if A[x] == 0:
                return x
        return -1

    left = K
    count = 0
    last = -1
    maxCount = 0
    for i in range(len(A)):
        if A[i] == 1:
            count += 1
        else:
            if left > 0:
                count += 1
                if last == -1:
                    last = i
                left -= 1
            else:
                # print("i: "+str(i))
                maxCount = max(maxCount, count)
                if last == -1:
                    count = 0
                else:
                    count = i - last
                # print("previous last "+str(last))
                if last != -1:
                    c = findzero(A, last, i)
                    if c == -1:
                        last = -1
                    else:
                        last = c
                # print("Changing last to "+ str(last))
                # print("Count: "+str(count))
                # count +=1

    return max(maxCount, count)
