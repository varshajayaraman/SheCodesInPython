class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        if len(A) == 1:
            return 0
        rotA0A = math.inf
        for i in range(1, len(A)):
            if A[i] == A[0]:
                if i == len(A) - 1:
                    if rotA0A == math.inf:
                        rotA0A = 0
                continue
            elif B[i] == A[0]:
                if rotA0A == math.inf:
                    rotA0A = 1
                else:
                    rotA0A += 1
            else:
                rotA0A = math.inf
                break

        rotB0A = math.inf
        for i in range(len(A)):
            if A[i] == B[0]:
                if i == len(A) - 1:
                    if rotB0A == math.inf:
                        rotB0A = 0
                continue
            elif B[i] == B[0]:
                if rotB0A == math.inf:
                    rotB0A = 1
                else:
                    rotB0A += 1
            else:
                rotB0A = math.inf
                break

        rotB0B = math.inf
        for i in range(1, len(B)):
            if B[i] == B[0]:
                if i == len(B) - 1:
                    if rotB0B == math.inf:
                        rotB0B = 0
                continue
            elif A[i] == B[0]:
                if rotB0B == math.inf:
                    rotB0B = 1
                else:
                    rotB0B += 1
            else:
                rotB0B = math.inf
                break

        rotA0B = math.inf
        for i in range(len(B)):
            if B[i] == A[0]:
                if i == len(B) - 1:
                    if rotA0B == math.inf:
                        rotA0B = 0
                continue
            elif A[i] == A[0]:
                if rotA0B == math.inf:
                    rotA0B = 1
                else:
                    rotA0B += 1
            else:
                rotA0B = math.inf
                break

        if min(rotA0A, rotA0B, rotB0A, rotB0B) == math.inf:
            return -1
        return min(rotA0A, rotA0B, rotB0A, rotB0B)