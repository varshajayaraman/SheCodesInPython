class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def rec(s, wordDict, start):
            global found, visited
            visited.add(s)
            if found:
                return

            if len(s) == 0:
                found = True
                return

            for w in wordDict:
                l = len(w)
                if s[:l] == w:
                    if s[l:] not in visited:
                        rec(s[l:], wordDict, start)
                        if found:
                            return

            # neigh = []

        global found, visited
        visited = set([])
        found = False
        rec(s, wordDict, 0)
        return found