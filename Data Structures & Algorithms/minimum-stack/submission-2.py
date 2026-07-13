class MinStack:

    def __init__(self):
        self.stack = []
        self.minATP = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minATP.append(val)
        else:
            self.stack.append(val)
            if val < self.minATP[len(self.minATP)-1]:
                self.minATP.append(val)
            else:
                self.minATP.append(self.minATP[len(self.minATP)-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minATP.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.minATP[len(self.minATP)-1]
        
