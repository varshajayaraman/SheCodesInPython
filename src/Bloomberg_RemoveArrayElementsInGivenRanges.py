import math
def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i - 1][1]:
            intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
            intervals.pop(i)
            print(intervals[i - 1])
        else:
            i += 1
    print(intervals)
    return intervals

def solution(arr, intervals):

    intervals=merge(intervals)
    i=0
    length = len(arr)
    while i<length:
        print("Looping: "+str(arr[i]))
        print(arr)
        x=bsearch(intervals,0,len(intervals)-1,arr[i])
        print("Status: "+str(x))
        if x:
            print("Popping "+str(i))
            arr.pop(i)

            length-=1
        else:
            i+=1
    return arr

def solution2(arr, intervals):

    intervals=merge(intervals)
    i=0
    length = len(arr)
    while i<length:
        print("Looping: "+str(i))
        print(arr)
        x=bsearch(intervals,0,len(intervals)-1,i)
        print("Status: "+str(x))
        if x:
            print("Popping "+str(i))
            arr[i]='x'
        i+=1
    arr = list(filter(lambda a:a!='x', arr))
    return arr

def bsearch(intervals, low,high, target):
    print(low,high)
    if low<=high:
        mid = low + math.floor((high-low)/2)
        print("Mid: "+str(mid))
        if target==intervals[mid][0] or (target > intervals[mid][0] and target<intervals[mid][1]):
            return True
        else:
            if target<intervals[mid][0]:
                print("In low")
                return bsearch(intervals,low,mid-1, target)
            else:
                return bsearch(intervals, mid+1, high, target)
    return False