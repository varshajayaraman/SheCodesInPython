def rotate(arr):
    row=len(arr)
    if row==0:
        return 0
    col = len(arr[0])
    maxRow = row-1
    maxCol = col-1
    i,j=0,0
    while i<maxRow-i:
        j=i
        while j<maxCol-i:
            print(i,j,maxRow,maxCol)
            ex = arr[i][j]
            # print(arr[i][j], arr[maxRow-j][i])
            arr[i][j] = arr[maxRow-j][i]
            # print(arr[maxRow-j][j],arr[maxRow-i][maxCol-j])
            arr[maxRow-j][i] = arr[maxRow-i][maxCol-j]
            # print(arr[maxRow-i][maxCol-j],arr[j][maxCol-i])
            arr[maxRow-i][maxCol-j] = arr[j][maxCol-i]
            # print(arr[j][maxCol-i],ex)
            arr[j][maxCol-i]  = ex
            # print(ex, arr[j][maxCol-i])
            j+=1
        print(arr)
        # maxRow -= 1
        # maxCol -= 1
        i+=1

    print(arr)