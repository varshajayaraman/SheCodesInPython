class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        if len(s) == 1:
            return "a"
        for c in range(len(s)):
            if s[c] == "?":
                if c == 0:
                    if "a" not in s[c + 1]:
                        s[c] = "a"
                    else:
                        s[c] = "b"
                elif c == len(s) - 1:
                    if "a" not in s[c - 1]:
                        s[c] = "a"
                    else:
                        s[c] = "b"
                else:
                    if "a" not in s[c + 1] and "a" not in s[c - 1]:
                        s[c] = "a"
                    elif "b" not in s[c + 1] and "b" not in s[c - 1]:
                        s[c] = "b"
                    else:
                        s[c] = "c"
        return "".join(s)
