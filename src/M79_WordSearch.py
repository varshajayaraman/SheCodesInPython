import math
def exist(board, word):
    def BFS(board, i, j, word, strind):
        # print("fresh iteration")
        row = len(board)
        col = len(board[0])
        queue = []
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        queue.append((i * col) + j)
        strind += 1
        childcount = 1
        nextchildcount = 0
        while len(queue) > 0:
            ele = queue.pop(0)
            # print("Ele: "+str(ele))
            childcount -= 1
            i = math.floor(ele / (col))
            j = (ele % (col))
            # if j>0:
            #     j-=1
            # print(i,j)
            print(i,j)
            visited[i][j] = 1
            # print(visited)
            if i < row - 1:

                if board[i + 1][j] == word[strind]:
                    # print("in1")
                    # print("Checking " + str(i + 1) + str(j))

                    if visited[i + 1][j] == 0:
                        if strind == len(word) - 1:
                            return True
                        queue.append(((i + 1) * (col)) + j )
                        nextchildcount += 1

            if i > 0:

                if board[i - 1][j] == word[strind]:
                    # print("in2")
                    # print("Checking " + str(i - 1) + str(j))

                    if visited[i - 1][j] == 0:
                        if strind == len(word) - 1:
                            return True
                        queue.append(((i - 1) * (col)) + j)
                        nextchildcount += 1

            if j > 0:

                if board[i][j - 1] == word[strind]:
                    # print("in3")
                    # print("Checking " + str(i) + str(j - 1))
                    if visited[i][j - 1] == 0:
                        if strind == len(word) - 1:
                            return True
                        queue.append(((i) * (col)) + j-1)
                        nextchildcount += 1

            if j < col - 1:

                if board[i][j + 1] == word[strind]:
                    # print("In4")
                    # print("Checking " + str(i) + str(j + 1))

                    if visited[i][j + 1] == 0:
                        if strind == len(word) - 1:
                            return True
                        # print("jvjhsd")
                        queue.append(((i) * (col)) + j + 1)
                        nextchildcount += 1

            # print(queue)
            if childcount == 0:
                childcount = nextchildcount
                nextchildcount = 0
                strind += 1
        return False

    row = len(board)
    col = len(board[0])
    strind = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[strind]:
                if BFS(board, i, j, word, strind):
                    return True
    return False