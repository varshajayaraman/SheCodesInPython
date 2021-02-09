class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path = path.split("/")
        last = -1
        for i in range(len(path)):
            p = path[i]
            if p == "..":
                if last >= 0:
                    res.pop(last)
                    last -= 1
                else:
                    continue
            elif len(p) == 0:
                continue
            elif p == ".":
                continue
            else:
                res.append(p)
                last += 1

        # print(res)
        return "/" + "/".join(res)