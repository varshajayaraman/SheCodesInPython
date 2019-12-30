class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = [int(x) for x in str(N)]
        for i in range(len(N)):
            if i + 1 < len(N):
                if N[i] > N[i + 1]:
                    while i > 0 and N[i] == N[i - 1]:
                        i -= 1
                    N[i] -= 1
                    # if N[i]==0:
                    i += 1
                    while (i < len(N)):
                        N[i] = 9
                        i += 1
                    break
        print(N)
        if len(N) == 0:
            return 0
        else:
            N = [str(i) for i in N]
            return int(''.join(N))
