class Solution:
    def numberOfMatches(self, n: int) -> int:
        global count
        count = 0

        def rec(n):
            global count
            print(n)
            if n == 0 or n == 1:
                return
            if n % 2 == 0:
                count += (n // 2)
                rec(n // 2)
            else:
                count += ((n - 1) // 2)
                rec(((n - 1) // 2) + 1)

        rec(n)
        return count