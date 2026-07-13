class MinStack:

    def __init__(self):
        self.stack = []
        self.min_at_that_index = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_at_that_index.append(val)
        else:
            if val < self.min_at_that_index[len(self.stack)-1]:
                self.min_at_that_index.append(val)
            else:
                prev_min = self.min_at_that_index[len(self.stack)-1]
                self.min_at_that_index.append(prev_min)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_at_that_index.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_at_that_index[len(self.stack)-1]
        
