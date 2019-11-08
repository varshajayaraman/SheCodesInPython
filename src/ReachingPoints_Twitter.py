flag=False
def wrapper(sx,sy,tx,ty):
    if canReach(sx,sy,tx,ty,flag):
        print("yes")
    else:
        print("no")
def canReach(sx,sy,tx,ty, flag):
    if flag==True:
        return True
    if sx==tx and sy==ty:
        flag= True
        return True
    if sx>tx or sy>ty:
        return

    return canReach(sx,sx+sy, tx,ty,flag) or canReach(sx+sy,sy,tx,ty,flag)
