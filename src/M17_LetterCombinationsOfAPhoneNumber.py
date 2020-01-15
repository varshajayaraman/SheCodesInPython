class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ref = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def recFn(digits, digInd, curr):
            if digInd == len(digits):
                if curr != "":
                    res.append(curr)
                return

            alphList = ref[digits[digInd]]
            for i in range(len(alphList)):
                recFn(digits, digInd + 1, curr + alphList[i])

        res = []
        curr = ""
        # alphList = ref[digits[0]]
        # for i in range(len(alphList)):
        #     curr += alphList[i]
        recFn(digits, 0, curr)
        print(res)
        return res