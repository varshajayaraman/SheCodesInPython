class Solution:
    def numSquares(self, n: int) -> int:
        table = [0]
        for i in range(1,n+1):
            table.append(math.inf)
        for j in range(1,int(math.sqrt(n+1))+1):
            for i in range(1,n+1):
                if j*j <=i:
                    table[i] = min(table[i], table[i-(j*j)]+1)
        return table[n]