def checkNextTwo(strs, ind, c):
    return strs[ind]==c and strs[ind+1]==c

def sol(strs):
    totalCount=0
    currCount=0
    # print(totalCount)
    for i in range(len(strs)):

        if i==0:
            currCount+=1
            continue
        if strs[i]==strs[i-1]:
            if currCount==2:
                if (i+1)<len(strs) and (i+2)<len(strs):
                    if strs[i]=='a':
                        res = checkNextTwo(strs, i+1, 'b')
                    else:
                        res = checkNextTwo(strs, i + 1, 'a')
                    totalCount+=1
                    print(totalCount)
                    if res:
                        currCount=0
                    else:
                        if strs[i+1]==strs[i]:
                            currCount=1
                        else:
                            currCount=0
                else:
                    totalCount += 1
                    break

            else:
                currCount+=1
        else:
            currCount=1
        print(i, totalCount, currCount)

    print(totalCount)