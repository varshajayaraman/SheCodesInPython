class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        lInd = -1
        maxRep = -1
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                lInd = i

        if lInd == -1:
            return A

        for i in range(lInd + 1, len(A)):
            if A[i] < A[lInd]:
                if maxRep == -1:
                    maxRep = i
                else:
                    if A[i] > A[maxRep]:
                        maxRep = i

        t = A[lInd]
        A[lInd] = A[maxRep]
        A[maxRep] = t
        # swap(A[lInd], A[maxRep])
        return A