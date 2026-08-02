class MinStack:

    def __init__(self):
        self.my_stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if len(self.mins) == 0 or val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1]) 

    def pop(self) -> None:
        self.my_stack.pop(-1)
        self.mins.pop(-1)

    def top(self) -> int:
        return self.my_stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
