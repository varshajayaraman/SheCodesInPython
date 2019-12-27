"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if id == 0:
            return 0
        global total
        total = 0
        imp = {}
        sub = {}
        for x in employees:
            imp[x.id] = x.importance
            sub[x.id] = x.subordinates

        # def dfs(imp, sub, curr):
        #     global total
        #     total += employees[curr-1].importance
        #     for x in employees[curr-1].subordinates:
        #         dfs(employees, x)

        def dfs(imp, sub, curr):
            global total
            total += imp[curr]
            for x in sub[curr]:
                dfs(imp, sub, x)

        dfs(imp, sub, id)
        print(total)
        return total