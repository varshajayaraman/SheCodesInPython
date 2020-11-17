	class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        arr = [p1,p2,p3,p4]
        
        def cmp_func(x,y):
            if x[1]==y[1]:
                return x[0]-y[0]
            else:
                x[1]-y[1]
                
        def dist(x,y):
            d=(y[0]-x[0])**2 + (y[1]-x[1])**2
            # print(x,y,d)
            return d
                #, key=lambda x:(x[1], x[0])
        arr=sorted(arr)
        # print(arr)
        if dist(arr[0],arr[1])>0 and dist(arr[0], arr[1])==dist(arr[0],arr[2]) and dist(arr[2],arr[3])==dist(arr[1], arr[3]) and dist(arr[0], arr[3])==dist(arr[1], arr[2]):
            return True
        return False
        