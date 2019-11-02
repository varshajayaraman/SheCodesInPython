import copy
class SnapshotArray:
    numList=[]
    snapList = []
    snaps=0
    def __init__(self, length: int):
        self.numList = [None]*length
    def set(self, index, val):
        self.numList[index] = val
    def snap(self) -> int:
        c=copy.deepcopy(self.numList)
        self.snapList.append(c)
        self.snaps+=1
        print(self.snaps-1)
        return self.snaps-1

    def get(self, index: int, snap_id: int) -> int:
        print(self.snapList)
        return self.snapList[snap_id][index];

# Your SnapshotArray object will be instantiated and called as such:
