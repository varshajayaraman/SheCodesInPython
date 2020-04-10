
def retrace(tab, s1, s2):
    r=len(tab)-1
    c=len(tab[0])-1
    res = []
    while r>=0 and c>=0:
        print(r, c)
        if s1[c]==s2[r]:
            print(s1[c], len(res))
            res.append(s1[c])
            r-=1
            c-=1
        elif r>=0 and tab[r-1][c]==tab[r][c]:
            r-=1
        else:
            if c>=0:
                c-=1
            else:
                print(res)
                return res


    return(res)

def LCS(s1, s2):

    l1 = len(s1)
    l2 = len(s2)
    tab = [[0 for i in range(l1)] for i in range(l2)]
    # print(tab)
    for i in range(l2):
        for j in range(l1):

            if s1[j]==s2[i]:
                if i==0 or j==0:
                    tab[i][j]=1
                else:
                    tab[i][j] = tab[i-1][j-1]+1
            else:
                if i==0:
                    tab[i][j] = tab[i][j-1]
                    continue
                elif j==0:
                    # print("Here: ", i,j)
                    tab[i][j] = tab[i-1][j]
                    continue
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])

    # for i in range(l2):
    #     r=[]
    #     for j in range(l1):
    #         r.append(tab[i][j])
    #     print(r)
    # print(tab)
    x=retrace(tab, s1, s2)
    print("Ans: ", len(x), x)
