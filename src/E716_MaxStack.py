class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.maxstack) == 0:
            self.maxstack.append(x)
        else:
            maxEle = max(self.maxstack[-1], x)
            self.maxstack.append(maxEle)

    def pop(self) -> int:
        if len(self.stack) > 0:
            self.maxstack.pop()
            return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def peekMax(self) -> int:
        if len(self.stack) > 0:
            return self.maxstack[-1]

    def popMax(self) -> int:
        if len(self.stack) > 0:
            maxEle = self.maxstack[-1]
            buffer = []
            while self.stack[-1] != self.maxstack[-1]:
                buffer.append(self.stack.pop())
                self.maxstack.pop()
            self.stack.pop()
            self.maxstack.pop()

            while len(buffer) > 0:
                self.push(buffer.pop())
                # self.stack.append(buffer.pop())

            return maxEle

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()