class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxFreq = 0
        maxLeng = 0
        i = 0
        st = 0
        ref = {}
        for i in range(len(s)):
            if ref.get(s[i]) is None:
                ref[s[i]] = 1
            else:
                ref[s[i]] += 1

            maxFreq = max(maxFreq, ref[s[i]])

            if i - st + 1 - maxFreq > k:
                ref[s[st]] -= 1
                st += 1
            else:
                maxLeng = max(maxLeng, i - st + 1)
        return maxLeng

