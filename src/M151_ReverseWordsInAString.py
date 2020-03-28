class Solution:
    def reverseWords(self, s: str) -> str:

        def reverseSentence(s):
            i = 0
            j = len(s) - 1
            while i < j:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i += 1
                j -= 1
            return s

        def getEnd(s, st):
            i = st
            while i < len(s) and s[i] != ' ':
                i += 1
            return i - 1

        def reverseWords(s):
            i = 0
            while i < len(s):
                while i < len(s) and s[i] == ' ':
                    # print(s)
                    i += 1
                j = getEnd(s, i)
                l = j
                # print(j)
                while i < j:
                    t = s[i]
                    s[i] = s[j]
                    s[j] = t
                    i += 1
                    j -= 1

                # print(s)
                i = l + 1

            return s

        def copy(st):
            word_seen = False
            li = []
            for i in range(len(st)):
                if st[i] == ' ' and i + 1 < len(st) and st[i + 1] == ' ':
                    continue
                elif st[i] == ' ' and word_seen is False:
                    continue
                word_seen = True
                li.append(st[i])
            if len(li) == 0:
                return li
            if li[len(li) - 1] == ' ':
                li.pop(len(li) - 1)
            return li

        st = s
        # if len(st)==0:
        #     return st
        s = copy(st)
        print(s)
        s = reverseSentence(s)
        print(s)
        s = reverseWords(s)
        return ''.join(s)