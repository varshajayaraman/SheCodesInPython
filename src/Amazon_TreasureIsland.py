import math
# global minStep
minStep = math.inf
def dfs(r,c,arr,step,row, col):
    #Up, Down, Left, Right

    global minStep
    arr[r][c] = step
    if r>0:
        if arr[r - 1][c] == 'X':
            print(r, c, step+1)
            minStep = min(minStep, step+1)
        if arr[r-1][c]=='O':
            dfs(r-1, c, arr, step+1, row, col)
    if r<row-1:
        if arr[r + 1][c] == 'X':
            minStep = min(minStep, step+1)
            print(r, c, step + 1)
        if arr[r+1][c]=='O':
            dfs(r+1, c, arr, step+1, row, col)
    if c>0:
        if arr[r][c-1] == 'X':
            minStep = min(minStep, step+1)
            print(r, c, step + 1)
        if arr[r][c-1]=='O':
            dfs(r, c-1, arr, step+1, row, col)
    if c<col-1:
        if arr[r][c+1] == 'X':
            minStep = min(minStep, step+1)
            print(r, c, step + 1)
        if arr[r][c+1]=='O':
            dfs(r, c+1, arr, step+1, row, col)
    # print(step)


def bfs(r,c, arr, step, row, col):
    global minStep
    q = []

    q.append((r,c, step))
    while len(q)>0:
        curr = q.pop(0)
        r = curr[0]
        c = curr[1]
        step = curr[2]
        arr[r][c] = step
        print(r,c,step, arr[r][c])
        if r > 0:
            if arr[r - 1][c] == 'X':
                print(r, c, step + 1)
                minStep = min(minStep, step + 1)
            if arr[r - 1][c] == 'O':
                q.append((r-1, c, step+1))
        if r < row - 1:
            if arr[r + 1][c] == 'X':
                minStep = min(minStep, step + 1)
                print(r, c, step + 1)
            if arr[r + 1][c] == 'O':
                q.append((r + 1, c, step + 1))
        if c > 0:
            if arr[r][c - 1] == 'X':
                minStep = min(minStep, step + 1)
                print(r, c, step + 1)
            if arr[r][c - 1] == 'O':
                q.append((r, c - 1, step + 1))
        if c < col - 1:
            if arr[r][c + 1] == 'X':
                minStep = min(minStep, step + 1)
                print(r, c, step + 1)
            if arr[r][c + 1] == 'O':
                q.append((r, c + 1, step + 1))





def findTreasure(arr):
    row=len(arr)
    if row==0:
        return 0
    col = len(arr[0])
    global minStep
    bfs(0,0,arr,0,row,col)
    print("Answer: ", minStep)