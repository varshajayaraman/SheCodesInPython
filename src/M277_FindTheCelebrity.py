# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        c = 0

        for i in range(1, n):
            if knows(c, i):
                c = i
        for i in range(n):
            if i == c:
                continue
            if not knows(i, c) or knows(c, i):
                return -1
        return c