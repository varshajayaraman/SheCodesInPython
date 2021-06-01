class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        global res, visited
        visited = set([])
        hmap = dict()
        email_name = dict()
        res = []

        def formDict():
            for a in accounts:
                email_name[a[1]] = a[0]
                first_em = a[1]
                if hmap.get(first_em) is None:
                    hmap[first_em] = set([])
                for e in a[2:]:
                    # print(first_em, e)
                    hmap[first_em].add(e)
                    if hmap.get(e) is None:
                        hmap[e] = set([])
                    hmap[e].add(first_em)

        def dfs(curr):
            # print(curr)
            global visited
            path = set([])
            if hmap.get(curr) is None:
                return set([])

            for c in hmap[curr]:
                if c not in visited:
                    visited.add(c)
                    x = dfs(c)
                    # print(path)
                    path.update(x)
                    path.add(c)
                    # print(path)
            path.add(curr)
            # print(path)
            return path

        formDict()
        # print(hmap)
        # print(email_name)
        for k, v in email_name.items():
            if k not in visited:
                # path = set([])
                emails = dfs(k)
                print(emails)
                emails = sorted(emails)
                emails.insert(0, v)
                res.append(emails)
        return res