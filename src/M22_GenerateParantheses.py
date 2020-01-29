class Solution:
    def rec(self, left, right, curr, n):
        global res

        if left == 0 and right == 0:
            res.append(curr)

        if left > 0 and right > 0:
            self.rec(left - 1, right, curr + "(", n)
        if right > 0 and left < n and right > left:
            self.rec(left, right - 1, curr + ")", n)

    def generateParenthesis(self, n: int) -> List[str]:
        global left, right, res
        left = n
        right = n
        res = []

        self.rec(left, right, "", n)
        return res