class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        refDict = {}

        for s in strs:
            # charList = [0 for i in range(26)]
            # for c in s:
            #     charList[ord(c)-ord('a')] +=1
            # if tuple(charList) not in refDict:
            #     refDict[tuple(charList)] = [s]
            # else:
            #     refDict[tuple(charList)].append(s)

            sortedS = "".join(sorted(s))
            if sortedS in refDict:
                refDict[sortedS].append(s)
            else:
                refDict[sortedS] = [s]

        res = []
        for k, v in refDict.items():
            res.append(v)

        return res