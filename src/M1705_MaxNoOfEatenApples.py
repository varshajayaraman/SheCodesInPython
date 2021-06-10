class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        def rec(A, D):
            i = 0
            fin = 0
            curr = []
            heapq.heapify(curr)
            while len(curr) > 0 or i < len(A):
                if i < len(A):
                    heapq.heappush(curr, [D[i] + i, A[i]])
                while len(curr) > 0:
                    # print(curr)
                    if curr[0][1] == 0 or curr[0][0] <= i:
                        heapq.heappop(curr)
                    else:
                        break

                if len(curr) > 0:
                    # print(i, curr)
                    curr[0][1] -= 1
                    fin += 1
                    # print(fin)
                i += 1

            return fin

        return rec(apples, days)