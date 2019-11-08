def leadingpt(scores):
    score1=0
    score2=0
    for x in scores:
        if x==0:
            score2-=1
        else:
            score2+=1

    if score1>score2:
        print(0)
        return
    for i in range(0,len(scores)):
        if scores[i]==1:
            score1 += 1
            score2 -= 1
        else:
            score1 -=1
            score2 += 1
        if score1>score2:
            print(i+1)
            break

