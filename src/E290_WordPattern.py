def wordPattern(self, pattern: str, str: str) -> bool:
    hmap = {}

    str = str.split()
    if len(str) != len(pattern):
        return False
    for i in range(len(pattern)):
        if hmap.get(pattern[i]):
            if str[i] != hmap[pattern[i]]:
                return False
        elif str[i] in hmap.values():
            return False
        else:
            hmap[pattern[i]] = str[i]
    return True