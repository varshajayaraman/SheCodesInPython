def decode(st):
    res = []
    for x in st:
        if x!= ']':
            res.append(x)
        else:

            ch = ""
            ent=len(res)-1
            while(res[ent]!='['):
                ch = res[ent]+ch
                res.pop(ent)
                ent=len(res)-1
            print("ch "+ch)
            res.pop(ent)
            times=""
            num=len(res)-1
            while num>=0 and res[num].isnumeric():
                times = res[num]+times
                print("times " + str(times))
                res.pop(num)
                num=len(res)-1
                print(res, num)
            times = int(times)
            a=""
            while(times>0):
                a += ch
                times-=1

            res.append(a)
        print(res)
    print("".join(res))


