def sol(strs):
    res=""
    i=0
    while i < len(strs)-1:
        if strs[i]>strs[i+1]:
            break
        else:
            res+=strs[i]
        i+=1
    if i == len(strs)-1:
        return res
    for j in range(i+1, len(strs)):
        res+=strs[j]
    return res