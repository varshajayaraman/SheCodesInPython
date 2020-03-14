class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def isempty(self, s):
        return len(s) == 0

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.isempty(self.s2):
            while not self.isempty(self.s1):
                self.s2.append(self.s1[-1])
                self.s1.pop(-1)
        e = self.s2.pop(-1)
        return e

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.isempty(self.s2):
            while not self.isempty(self.s1):
                self.s2.append(self.s1[-1])
                self.s1.pop(-1)
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.isempty(self.s1) and self.isempty(self.s2)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()