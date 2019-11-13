import math
def exist(board, word):
    def DFS(board, i, j, visited, word, strind):
        # print("fresh iteration")
        row = len(board)
        col = len(board[0])

        strind += 1
        if strind == len(word):
            return True
        visited[i][j] = 1
        if i < row - 1:
            if board[i + 1][j] == word[strind]:
                if visited[i + 1][j] == 0:
                    if strind == len(word) - 1:
                        return True
                    if DFS(board,i+1,j,visited,word,strind):
                        return True
                    else:
                        visited[i+1][j] = 0

        if i > 0:
            if board[i - 1][j] == word[strind]:
                if visited[i - 1][j] == 0:
                    if strind == len(word) - 1:
                        return True
                    if DFS(board,i-1,j,visited,word,strind):
                        return True
                    else:
                        visited[i-1][j] = 0

        if j > 0:
            if board[i][j - 1] == word[strind]:
                if visited[i][j - 1] == 0:
                    if strind == len(word) - 1:
                        return True
                    if DFS(board,i,j-1,visited,word,strind):
                        return True
                    else:
                        visited[i][j-1] = 0

        if j < col - 1:
            if board[i][j + 1] == word[strind]:
                if visited[i][j + 1] == 0:
                    if strind == len(word) - 1:
                        return True
                    if DFS(board,i,j+1,visited,word,strind):
                        return True
                    else:
                        visited[i][j+1] = 0

        return False

    row = len(board)
    col = len(board[0])
    strind = 0
    visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[strind]:
                if DFS(board, i, j, visited, word, strind):
                    return True
                else:
                    visited[i][j] = 0
    return False