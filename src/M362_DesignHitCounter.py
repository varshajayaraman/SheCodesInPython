class DoublyNode:

    def __init__(self, t, v):
        self.time = t
        self.count = v
        self.next = None
        self.prev = None


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}
        self.head = None
        self.last = None

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.hmap:
            self.hmap[timestamp].count += 1

        else:
            self.hmap[timestamp] = DoublyNode(timestamp, 1)
            self.hmap[timestamp].next = None
            if self.last:
                self.last.next = self.hmap[timestamp]

            self.hmap[timestamp].prev = self.last
            self.last = self.hmap[timestamp]

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        # for i in range(timestamp, timestamp-6, -1):
        #     if i in self.hmap:
        #         count += self.hmap[i]
        curr = self.last
        if timestamp in self.hmap:
            curr = self.hmap[timestamp]
        # else:
        #     curr = self.last

        i = 0
        while curr and curr.time > timestamp - 300:
            count += curr.count
            curr = curr.prev

        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)