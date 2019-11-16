def compareVersion(self, version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")
    print(v1, v2)
    i = 0
    while i < min(len(v1), len(v2)):
        if int(v1[i]) < int(v2[i]):
            return -1
        elif int(v1[i]) > int(v2[i]):
            return 1
        i += 1
    print(i)
    if len(v1) == len(v2):
        return 0
    if len(v1) == i:
        while i < len(v2) and int(v2[i]) == 0:
            i += 1
        if i == len(v2):
            return 0
        else:
            return -1
    else:
        while i < len(v1) and int(v1[i]) == 0:
            i += 1
        if i == len(v1):
            return 0
        else:
            return 1
