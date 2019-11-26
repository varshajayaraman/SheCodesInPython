import heapq
def solution(stream):
    heap=[]
    min=1
    # heap.append(stream[0])
    # heapq.heapify(heap)
    for x in stream:
        if x[0]==min:
            print(x)
            min+=1
        else:
            heapq.heappush(x)
        if len(heap)>0:
            while heap[0][0] == min:
                print(heapq.heappop(heap))
                min+=1

        else:
            heapq.heappush(heap)
    while len(heap)>0:
        print(heapq.heappop(heap))
