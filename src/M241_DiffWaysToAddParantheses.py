class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def rec(start, end):

            if start >= len(input):
                return []
            res = list()
            for i in range(start, end):
                if input[i].isdigit() is False:
                    l1 = rec(start, i)
                    l2 = rec(i + 1, end)

                    for a in l1:
                        for b in l2:
                            if input[i] == "+":
                                res.append(a + b)
                            elif input[i] == "-":
                                res.append(a - b)
                            elif input[i] == "*":
                                res.append(a * b)
            if len(res) == 0:
                # print(start, end)
                res.append(int(input[start:end]))
            return res

        return rec(0, len(input))