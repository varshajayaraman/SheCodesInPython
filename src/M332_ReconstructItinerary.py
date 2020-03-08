class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        global ref, res, trips, visited
        trips = len(tickets) + 1
        ref = {}
        visited = {}
        for t in tickets:
            if t[0] in ref:
                ref[t[0]].append(t[1])
            else:

                ref[t[0]] = [t[1]]

        for k in ref.keys():
            ref[k].sort()

        # print(tickets)
        for k, v in ref.items():
            visited[k] = [False for i in range(len(v))]

        # print(ref)

        def dfs(iti):
            # print(iti)
            global ref, trips, visited, res
            if len(iti) == trips:
                res = iti
                return
            curr = iti[-1]
            if curr in ref:
                for i in range(len(visited[curr])):
                    if not visited[curr][i]:
                        visited[curr][i] = True
                        dfs(iti + [ref[curr][i]])
                        if res:
                            return
                        visited[curr][i] = False
            else:
                return

        # global res
        res = None
        dfs(["JFK"])
        return res