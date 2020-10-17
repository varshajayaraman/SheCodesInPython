class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        def intersection(a,b):
            #print("b", a, b)
            res = []
            if b[0]<=a[1]:
                res.append(b[0])
            else:
                return []
            if b[1]<a[1]:
                res.append(b[1])
            else:
                res.append(a[1])
            #print(res)
            return res
        
        if len(points)==0:
            return 0
        points.sort(key = lambda a: a[0])
        print(points)
        res = 0
        b=points.pop(0)
        while len(points)>0:
            #print(points)
            p1 = points.pop(0)
            a = intersection(b,p1)
            if len(a)==0:
                res+=1
                b=p1
                #print("After", b, points)
            else:
                b=a
        return res+1