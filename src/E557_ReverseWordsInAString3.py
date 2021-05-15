class Solution:
    def reverseWords(self, s: str) -> str:

        def find_word(s, start):
            i = -1
            while (start + i + 1) < len(s) and s[start + i + 1] != ' ':
                i += 1
            if i == -1:
                return start, -1
            return start, start + i

        res = [i for i in s]
        st = 0
        e = 0
        while 1:
            st, e = find_word(s, st)
            end = e
            # print(st, e)
            if e == -1:
                break

            while st < e:
                t = res[st]
                res[st] = res[e]
                res[e] = t
                st += 1
                e -= 1
            st = end + 2
        return "".join(res)