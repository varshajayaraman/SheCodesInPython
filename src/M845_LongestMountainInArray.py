class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        l = 1
        maxL = 0
        greater_slope = True
        onePass = False
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                if greater_slope:
                    if not onePass:
                        onePass=True
                    l+=1
                else:
                    greater_slope=True
                    maxL = max(maxL, l)
                    l=2
            elif arr[i]==arr[i-1]: #breaks uphill
                onePass=False
                if not greater_slope:
                    maxL = max(maxL, l)
                l=1
                greater_slope=True
                continue
            else:
                if not onePass or i==1:
                    maxL = max(maxL, l)
                    l=1
                    continue
                if greater_slope: #i=1 or after peak
                    # if onePass:
                    greater_slope=False
                        
                    
                # print(i)
                l+=1
        if not greater_slope:
            maxL = max(maxL, l)
        if maxL==1:
            return 0
        return maxL
                
                    