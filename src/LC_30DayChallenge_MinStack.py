class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)

        else:
            if x <= self.minStack[len(self.minStack) - 1]:
                self.minStack.append(x)

    def pop(self) -> None:
        p = self.stack[len(self.stack) - 1]
        self.stack.pop()
        if p == self.minStack[len(self.minStack) - 1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()