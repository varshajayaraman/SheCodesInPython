def dfs(adjMat, visited, finished, i, j, row, col):
        print("Visiting Node: "+str(i)+str(j))
        # print("Status: "+str(visited[j]))
        # print(visited)
        # print(finished)
        visited[i]=True
        # print(finished)
        if finished[j]:
            # print("Glee")
            finished[i] = True
            return finished, True

        else:
            if not visited[j]:
                # print("In")
                visited[j] = True
                # print(finished)
                for c in range(col):
                    # print(c)
                    # print(finished)
                    if adjMat[j][c] == 1:

                        finished, res = dfs(adjMat, visited, finished, j, c, row, col)
                        # print(res)
                        if res==False:
                            return finished, False
                        else:
                            # print("Glee1")
                            finished[j]=True
                            # finished[i]=True
                            return finished, True
                # print("Glee3")
                finished[j]=True
                # finished[i]=True
                return finished, True
            else:
                # print("Here")
                return finished, False


def canFinish(numCourses, prerequisites):

        pr = prerequisites
        adjMat = [[False for j in range(numCourses)] for i in range(numCourses)]
        finished = [False for i in range(numCourses)]
        visited = [False for i in range(numCourses)]
        count = 0
        row = len(adjMat)
        if row == 0:
            return True
        col = len(adjMat[0])
        nondep_courses = 0
        for i in range(len(prerequisites)):
            if len(pr[i]) > 1:
                for j in range(len(pr[i])):
                    course = pr[i][0]
                    dep = pr[i][1]
                    if adjMat[dep][course]:
                        return False
                    else:
                        adjMat[course][dep] = True
            else:
                nondep_courses+=1
        print(adjMat)
        flag=0
        for i in range(len(adjMat)):
            for j in range(len(adjMat[0])):
                if adjMat[i][j] == 1:
                    # print(finished)
                    flag=1
                    finished, res = dfs(adjMat, visited, finished, i, j, row, col)
                    # print(res)
                    if res == False:
                        return False
            if flag==1:
                finished[i]=True
                flag=0
            print(finished)

        for x in finished:
            if x:
                count += 1
                if (count+nondep_courses) == numCourses:
                    return True

        return False

