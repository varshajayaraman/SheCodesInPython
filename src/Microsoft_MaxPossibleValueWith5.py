def maxPositive(num):
    print("Pos")
    dip=False
    sNum = str(num)
    for i in range(len(sNum)):
        if sNum[i]< '5':
            if i==0:
                sNum = '5'+sNum
                return sNum
            else:
                sNum=sNum[0:i]+'5'+sNum[i:]
                return sNum
    sNum +='5'
    return sNum
def maxNegative(num):
    print("Neg")
    ind = 0
    sNum = str(num)
    for i in range(1,len(sNum)):
        if sNum[i] > '5':
            sNum = sNum[0:i] + '5' + sNum[i:]
            return sNum
    sNum += '5'
    return sNum
def sol(num):
    if num >0:
        print(maxPositive(num))
    elif num==0:
        print(50)
    else:
        print(maxNegative(num))