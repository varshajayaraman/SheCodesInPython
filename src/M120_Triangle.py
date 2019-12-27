class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        row = len(triangle)
        if row == 1:
            return triangle[0][0]

        j = 1
        for i in range(len(triangle) - 1):
            t = [i for i in triangle[i + 1]]
            # print(t, triangle)
            # print("next row begore modif: ", t)
            for j in range(len(triangle[i])):
                if j > 0:
                    # if i==len(triangle)-2 and j==1:
                    #     print(i, t, "min: ", t[j]+triangle[i][j], triangle[i+1][j])
                    triangle[i + 1][j] = min(t[j] + triangle[i][j], triangle[i + 1][j])
                    triangle[i + 1][j + 1] = triangle[i][j] + triangle[i + 1][j + 1]
                else:
                    triangle[i + 1][j] = triangle[i][j] + triangle[i + 1][j]
                    triangle[i + 1][j + 1] = triangle[i][j] + triangle[i + 1][j + 1]
        #     print("row: ", triangle[i])
        #     print("next row: ", triangle[i+1])
        # print("row: ", triangle[len(triangle)-1])
        return (min(triangle[len(triangle) - 1]))