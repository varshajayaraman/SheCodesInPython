class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magMap = dict()
        for m in magazine:
            if magMap.get(m) is None:
                magMap[m] = 0
            magMap[m] += 1

        for r in ransomNote:
            if magMap.get(r) is None or magMap[r] == 0:
                return False
            magMap[r] -= 1
        return True