class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def new_m():
            ans = []

            for j in range(len(num2) - 1, -1, -1):
                curr_p = 0
                carry = 0
                power = 0
                for i in range(len(num1) - 1, -1, -1):
                    n1 = num1[i]
                    n2 = num2[j]
                    p = carry + (int(n1) * int(n2))
                    carry = p // 10
                    p = p % 10
                    curr_p = (p * pow(10, power)) + curr_p
                    power += 1
                if carry > 0:
                    curr_p = carry * pow(10, power) + curr_p
                ans.append(curr_p)

            # print(ans)
            tot = 0
            for i in range(len(ans)):
                tot = (ans[i] * pow(10, i)) + tot
            return str(tot)

        return new_m()

        def arra():
            ans = [0 for i in range(len(num1) + len(num2))]
            pos = len(ans) - 1

            for j in range(len(num2) - 1, -1, -1):
                c = 0
                carry = 0
                for i in range(len(num1) - 1, -1, -1):
                    n1 = num1[i]
                    n2 = num2[j]
                    a = carry + (int(n1) * int(n2))
                    ans[pos - c] += a
                    carry = (ans[pos - c] // 10)
                    ans[pos - c] = ans[pos - c] % 10
                    c += 1
                if carry > 0:
                    ans[pos - c] = carry
                pos -= 1
                # print(ans)

            for i in range(len(ans)):
                if ans[i] != 0:
                    break
            n = [str(k) for k in ans[i:]]
            # n.reverse()
            return "".join(n)