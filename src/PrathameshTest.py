import heapq
def func2(arrival, duration):
    heap = []
    heapq.heapify(heap)
    for i in range(len(arrival)):
        heapq.heappush(heap, [arrival[i]+duration[i], arrival[i], duration[i]])

    prev_end = 0
    count = 0
    while len(heap)>0:
        curr=heapq.heappop(heap)
        if curr[1]>=prev_end:
            count+=1
            prev_end = curr[1]+curr[2]

    print( count)

def func3(arr):
    n_arr = [0 for i in arr]
    n_arr[0]=1
    maxVal = 0
    for i in range(1,len(arr)):
        curr = 1
        for j in range(i):
            if arr[j]<arr[i]:
                curr=max(n_arr[j]+1, curr)
        n_arr[i]=(curr)
        maxVal = max(maxVal, curr)

    print(n_arr)
    if maxVal==len(arr):
        print(0)
    else:
        print(len(arr)-maxVal-1)

def func(arr):
    prev = [0 for i in arr]
    count = 0
    for x in arr:
        i, j = 0, count
        while i != j:
            mid = (i + j) // 2
            if prev[mid] >= x:
                j=mid
            else:
                i = mid + 1
        prev[i] = x
        count = max(i + 1, count)
    print(count)
    if count==len(arr):
        return 0
    else:
        return len(arr)-count-1
