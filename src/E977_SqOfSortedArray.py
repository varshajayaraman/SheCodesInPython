class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        neg = []

        pos = []

        for n in A:
            if n < 0:
                neg.append(n * n)
            else:
                pos.append(n * n)

        res = []

        i = len(neg) - 1
        j = 0

        while i >= 0 and j < len(pos):
            if neg[i] < pos[j]:
                res.append(neg[i])
                i -= 1
            elif neg[i] > pos[j]:
                res.append(pos[j])
                j += 1
            else:
                res.append(neg[i])
                res.append(pos[j])
                i -= 1
                j += 1

        while i >= 0:
            res.append(neg[i])
            i -= 1

        while j < len(pos):
            res.append(pos[j])
            j += 1

        print(neg, pos)
        return res