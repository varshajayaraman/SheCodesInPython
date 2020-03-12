class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [0 for i in range(2069)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ind = key % 2069

        if self.arr[ind] == 0:
            self.arr[ind] = [[key, value]]
        else:
            for i in (self.arr[ind]):
                if i[0] == key:
                    i[1] = value
                    return
            self.arr[ind].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        ind = key % 2069

        if self.arr[ind] == 0:
            return -1
        # ptint()
        for i in ((self.arr[ind])):
            if i[0] == key:
                return i[1]

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        ind = key % 2069
        if self.arr[ind] == 0:
            return
        i = 0
        while i < len(self.arr[ind]):
            if self.arr[ind][i][0] == key:
                self.arr[ind].pop(i)
                break
            i += 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)