class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=list(t)
        t.sort()
        s=list(s)
        s.sort()
        print(s,t)
        return  s==t