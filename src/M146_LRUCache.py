from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.ref = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.ref:
            self.ref.move_to_end(key, last=True)
            return self.ref[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ref:
            self.ref[key]=value
            self.ref.move_to_end(key, last=True)
            return
        elif len(self.ref.keys())==self.capacity:
            self.ref.popitem(last=False)
        self.ref[key]=value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)