class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []

        for i in S:
            if i == "(":
                stack.append(i)
            else:
                ans = 0
                while stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
                stack.append(max(2 * ans, 1))
        print(stack)
        return sum(stack)