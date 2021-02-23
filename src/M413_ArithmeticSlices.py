class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        res = [[0, 1] for i in A]
        if len(A) == 0 or len(A) == 1:
            return count
        # res[1] = [(A[1]-A[0]), 2]

        for i in range(1, len(A)):
            diff = (A[i] - A[i - 1])
            if diff == res[i - 1][0]:
                res[i] = [diff, res[i - 1][1] + 1]
            else:
                res[i] = [diff, 2]
            if res[i][1] > 2:
                count += 1 + (res[i][1] - 3)
        # print(res)
        return count



