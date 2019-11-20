class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        if not s:
            return 0
        maxl = -math.inf
        mini = -1
        res = {}
        for i in range(len(s)):

            if s[i] not in res.keys():
                print(s[i])
                res[s[i]] = i
                l += 1
            else:
                if res[s[i]] < mini:
                    print("Index lesser: ")
                    print(res[s[i]], i, mini)
                    res[s[i]] = i
                    l += 1
                else:
                    if mini == -1:
                        mini = 0
                    print("Index greater")
                    print(res[s[i]], i, mini)
                    maxl = max(l, maxl)
                    mini = res[s[i]]
                    l = i - mini
                    print("new l: " + str(l))
                    res[s[i]] = i
        print(l, maxl)
        maxl = max(maxl, l)
        print(res, mini)
        return maxl
