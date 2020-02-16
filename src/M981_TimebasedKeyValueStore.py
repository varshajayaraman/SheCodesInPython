import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ref = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ref:
            self.ref[key] = {}
            self.ref[key][timestamp] = value
        else:
            self.ref[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        def bsearch(time, li, l, h):
            # print(l,h)
            if l <= h:
                m = l + ((h - l) // 2)

                if li[m] < time:
                    if m + 1 > h:
                        return li[m]
                    if m + 1 <= h and li[m + 1] > time:
                        return li[m]
                    else:
                        return bsearch(time, li, m + 1, h)
                elif li[m] > time:

                    if m - 1 >= l and li[m - 1] < time:
                        return li[m]
                    else:
                        return bsearch(time, li, l, m - 1)

            else:
                return -1

        if key not in self.ref:
            return ""
        else:
            # if timestamp in self.ref[key]:
            #     return self.ref[key][timestamp]
            l = list(self.ref[key].keys())
            # print(self.ref)
            # ind = bsearch(timestamp, l, 0, len(l)-1)

            ind = bisect.bisect_right(l, timestamp)
            if ind == 0:
                return ""
            else:
                # print(ind, key)
                return self.ref[key][l[ind - 1]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)