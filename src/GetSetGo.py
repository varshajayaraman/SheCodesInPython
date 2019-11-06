
def solution(cal, sum, ind):
    x= rec(cal, sum, ind)
    print(1)
    print(x)

def rec(cal, sum, ind):
    print(cal, sum, ind)
    if len(cal)==0 or sum<0:
        return False

    if sum==0:
        return True
    else:
        for i in range(ind, len(cal)):
            if rec(cal, sum - cal[i], i+1):
                return True
    return False