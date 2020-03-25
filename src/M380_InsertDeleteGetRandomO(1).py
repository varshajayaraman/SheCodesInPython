class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = []
        self.hmap = {}
        self.r = Random()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.hmap.get(val) is not None:
            return False

        self.li.append(val)
        self.hmap[val] = len(self.li) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if self.hmap.get(val) is None:
            return False

        if len(self.li) == 1:
            self.li.pop(0)
            # del self.hmap[val]
        elif self.li[len(self.li) - 1] == val:
            self.li.pop(len(self.li) - 1)
        else:
            last = self.li[len(self.li) - 1]
            self.li[self.hmap[val]] = last
            self.li.pop(len(self.li) - 1)
            ind = self.hmap[val]
            self.hmap[last] = ind
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.li[self.r.randint(0, len(self.li) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()