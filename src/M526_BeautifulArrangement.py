class Solution:
    def countArrangement(self, n: int) -> int:
        global count
        refSet = [-1]
        count = 0

        for i in range(1, n + 1):
            refSet.append(i)

        def rec(curr_index, refSet):

            global count

            for i in range(1, len(refSet)):
                if refSet[i] > 0 and refSet[i] % curr_index == 0:
                    # print(curr_index, refSet)
                    if curr_index == n:
                        count += 1
                        return
                    refSet[i] = -1
                    rec(curr_index + 1, refSet)
                    refSet[i] = i
                elif refSet[i] > 0 and curr_index % refSet[i] == 0:
                    if curr_index == n:
                        count += 1
                        return
                    refSet[i] = -1
                    rec(curr_index + 1, refSet)
                    refSet[i] = i

        rec(1, refSet)
        return count