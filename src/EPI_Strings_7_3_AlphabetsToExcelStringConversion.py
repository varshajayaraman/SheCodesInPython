def convert(st):
    mapp = {}
    i = 1
    for a in "abcdefghijklmnopqrstuvwxyz":
        mapp[a]=i
        i+=1
    res=0
    le = len(st)-1
    # res = (le-1)*26*mapp[s[]]
    print(pow(2,26), 26**2, 26*26)
    for i in range(len(st)):
        if i+1<len(st):
            if (mapp[st[i]]-1) !=0:
                res += 26**(le-i) * (mapp[st[i]])
            else:
                res += (le-1 - i) * 26*26
            print(res)
        else:
            print("Adding ", mapp[st[i]])
            res += mapp[st[i]]
    # if len(st)>1:
    #     print(res+26)
    # else:
        print(res)