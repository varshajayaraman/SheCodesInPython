def processQueries(self, queries: List[int], m: int) -> List[int]:
        def findPos(P, ele):
            for i in range(len(P)):
                if P[i]==ele:
                    return i
        def move(P, pos):
            ele = P[pos]
            for i in range(pos-1, -1, -1):
                P[i+1] = P[i]
            P[0] = ele
            return P
        
        res=[]
        P=[i for i in range(1,m+1)]
        for i in range(len(queries)):
            pos = findPos(P, queries[i])
            res.append(pos)
            P = move(P, pos)
        return res