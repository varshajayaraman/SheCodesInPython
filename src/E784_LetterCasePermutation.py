class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        res = {S}

        def toggle(s, i):
            if s[i].islower():
                return s[:i] + s[i].upper() + s[i + 1:]
            else:
                return s[:i] + s[i].lower() + s[i + 1:]

        def rec(item, res):
            # print(res)
            # global res
            for i in range(len(item)):
                if item[i].isalpha():
                    new = toggle(item, i)
                    if new in res:
                        continue
                    res.add(new)
                    rec(new, res)

        # for it in res:
        rec(S, res)
        print(res)
        return res