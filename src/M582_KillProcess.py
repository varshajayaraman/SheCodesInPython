class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def rec(currKill):
            global res
            # print(res)
            for k in cpRef[currKill]:
                if k not in res:
                    # print("Adding: ", k)
                    res.add(k)
                    if k in cpRef:
                        rec(k)

        cpRef = {}
        global res
        res = set([])
        for i in range(len(ppid)):
            parent = ppid[i]
            if parent not in cpRef:
                cpRef[parent] = []
            cpRef[parent].append(pid[i])

        # print(cpRef)
        if kill in cpRef:
            rec(kill)
        # print(res)
        res.add(kill)
        return res

        # res = []
        # i=0
        # while i<len(pid) and i<len(ppid):
        #     if ppid[i]==kill:
        #         res.append(pid[i])
        #     if pid[i]