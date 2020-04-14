class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        s = []

        if len(S) > 0:
            i = 0
            while i < len(S):
                if S[i] == '#':
                    if len(s) > 0:
                        s.pop()
                    i += 1
                else:
                    s.append(S[i])
                    i += 1

        t = []

        if len(T) > 0:
            i = 0
            while i < len(T):
                if T[i] == '#':
                    if len(t) > 0:
                        t.pop()
                    i += 1
                else:
                    t.append(T[i])
                    i += 1

        return s == t


