class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0

        if name[i] != typed[j]:
            print(i, j)
            return False
        while i + 1 < len(name) and j + 1 < len(typed):

            if name[i + 1] == typed[j + 1]:
                print(i)
                i += 1
                j += 1
                continue
            elif typed[j + 1] == typed[j]:
                j += 1
                continue
            else:
                return False

        if i + 1 < len(name):
            return False

        while j + 1 < len(typed):
            if typed[j + 1] == name[i]:
                j += 1
            else:
                return False
        return True