class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0 for x in range(len(graph))]
        state = [0 for x in range(len(graph))]
        for x in range(len(graph)):
            if len(graph[x]) == 0:
                state[x] = 1

        def dfs(graph, curr, visited, state):
            visited[curr] = 1
            for x in graph[curr]:
                if state[x] == 1:
                    continue
                if state[x] == -1:
                    state[curr] = -1
                    continue
                if visited[x] == 1:
                    state[x] = -1
                    state[curr] = -1
                    return
                dfs(graph, x, visited, state)
            for x in graph[curr]:
                if state[x] != 1:
                    return
            state[curr] = 1

        for m in range(len(graph)):
            dfs(graph, m, visited, state)
        print(state)
        for z in range(len(state)):
            if state[z] == 1:
                state[z] = z
            else:
                state[z] = -1
        state = filter(lambda l: l != -1, state)
        print(state)
        return state
