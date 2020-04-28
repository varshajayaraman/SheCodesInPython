class Solution:
    def reverseVowels(self, s: str) -> str:

        f = 0
        l = len(s) - 1
        new = ['' for x in s]
        while f <= l:
            while f <= l and s[f] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                new[f] = s[f]
                f += 1
            if f > l:
                return "".join(new)
            while f <= l and s[l] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                new[l] = s[l]
                l -= 1
            if f > l:
                return "".join(new)
            new[f] = s[l]
            new[l] = s[f]
            f += 1
            l -= 1

        return "".join(new)