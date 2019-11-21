class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        el = []
        if not s:
            return None
        for i in range(len(s)):
            if s[i].isalpha():
                print(i)
                continue
            else:
                if s[i] == '(':
                    el.append(('(', i))

                else:
                    if len(el) > 0:
                        last = el[len(el) - 1]
                        if '(' in last:
                            el.pop(len(el) - 1)
                        else:
                            el.append((')', i))
                    else:
                        el.append((')', i))
        i = len(s) - 1
        l = len(el) - 1
        print(el, s)
        newStr = ""
        while i >= 0 and l >= 0:
            if i in el[l]:
                newStr = s[:i] + s[i + 1:]
                l -= 1
                s = newStr
            i -= 1
            print(i, l)
        print(s)
        return s
