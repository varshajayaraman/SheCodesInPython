class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dom = list(dominoes)

        i = len(dom) - 1
        j = 0

        for x in range(len(dom)):
            if dom[x] == 'L' or dom[x] == 'R':
                if dom[x] == 'L':
                    j = x
                if dom[x] == 'R':
                    i = x

                while i < j:
                    dom[i] = 'R'
                    dom[j] = 'L'
                    i += 1
                    j -= 1
                    if j <= i:
                        j = 0
                        i = len(dom) - 1
        print(dom)
        rt = False
        for x in range(len(dom)):
            if dom[x] == 'R':
                rt = True
            if dom[x] == 'L':
                rt = False
            if dom[x] == '.' and rt:
                if x == len(dom) - 1 or dom[x + 1] != 'L':
                    dom[x] = 'R'

        rt = False
        for x in range(len(dom) - 1, -1, -1):
            if dom[x] == 'L':
                rt = True
            if dom[x] == 'R':
                rt = False
            if dom[x] == '.' and rt:
                if x == 0 or dom[x - 1] != 'R':
                    dom[x] = 'L'
        return "".join(dom)