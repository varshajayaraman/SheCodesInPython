#2-currently visiting
#1-visited

def rec(arr, i, j, row, col, currLoop):
    print(i,j, arr)
    global flag, visited
    if flag:
        return
    arr[i][j] = 2
    if j<col-1:
        if arr[i][j+1]==currLoop:
            rec(arr, i, j+1, row, col, currLoop)
            arr[i][j+1]=currLoop
            visited[(i, j+1)] = True
        elif arr[i][j+1]==2 and (i, j+1) in visited.keys():
            print("Setting flag in: ", i,j+1)
            flag=True
    if j>0:
        if arr[i][j-1]==currLoop:
            rec(arr, i, j-1, row, col, currLoop)
            arr[i][j - 1] = currLoop
            visited[(i, j-1)] = True
        elif arr[i][j-1]==2 and (i,j-1) in visited.keys():
            print("Setting flag in: ", i, j - 1)
            flag=True
    if i<row-1:
        if arr[i+1][j]==currLoop:
            rec(arr, i+1, j, row, col, currLoop)
            arr[i+1][j] = currLoop
            visited[(i+1, j)] = True
        elif arr[i+1][j]==2 and (i+1,j) in visited.keys():
            print("Setting flag in: ", i + 1, j)
            flag=True
    if i>0:
        if arr[i-1][j]==currLoop:
            rec(arr, i-1, j, row, col, currLoop)
            arr[i-1][j] = currLoop
            visited[(i-1, j)] = True
        elif arr[i-1][j]==2 and (i-1, j) in visited.keys():
            print("Setting flag in: ", i- 1, j)
            flag=True

def findLoops(arr):
    global found, flag, visited
    visited = {}
    found={}
    flag=False
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if (i,j) not in visited.keys() and arr[i][j] not in found.keys():
                print("New branch: ")
                currLoop = arr[i][j]
                rec(arr, i, j, row, col, currLoop)
                arr[i][j]=currLoop
                visited[(i,j)]=True
                if flag:
                    found[currLoop] = True
                    flag=False
            if arr[i][j] in found.keys():
                visited[(i,j)]=True
    print(found)