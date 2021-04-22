class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        global alph, res, d
        alph = ['a', 'b', 'c']
        res = []
        d = {}

        def rec(currList):
            global res, alph, d

            for i in range(len(alph)):
                if len(currList) > 0 and currList[-1] == alph[i]:
                    continue
                if len(res) == k:
                    return
                if len(currList + [alph[i]]) == n:
                    if d.get("".join(currList + [alph[i]])) is None:
                        res.append(currList + [alph[i]][:])
                        d["".join(currList + [alph[i]])] = 1
                    continue
                else:
                    rec(currList + [alph[i]])
                    continue

        rec([])
        if len(res) == k:
            return "".join(res[-1])
        return ""
