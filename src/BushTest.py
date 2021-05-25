def func(products):
    res = []
    d = {}

    for i in products:
        if d.get(i) is None:
            d[i]=1
        else:
            d[i] +=1

    d= {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    maxVal = 0
    for k,v in d.items():
        maxVal = v
        break
    for k,v in d.items():
        if v==maxVal:
            res.append(k)
        else:
            break
    res = sorted(res)
    print(res[-1])