class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j=0
        i=0
        while i>=0 and i<len(pushed):
            while pushed[i]==popped[j]:
                pushed.pop(i)
                j+=1
                i-=1
                if i<0:
                    break
            i+=1
        return len(pushed)==0