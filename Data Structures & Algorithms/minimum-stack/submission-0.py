class MinStack:

    def __init__(self):
        self.capacity = 1
        self.length  = 0
        self.stack = [0]*self.capacity
        self.stack_min = [0]*self.capacity


    def push(self, val: int) -> None:
        
        if self.length >= self.capacity:
            stack_tmp = self.stack
            stack_min_tmp = self.stack_min
            self.stack = [0]*self.capacity*2
            self.stack_min = [0]*(self.capacity*2)
            self.capacity = self.length*2
            for i in range(self.length):
                self.stack[i]=stack_tmp[i]
                self.stack_min[i]=stack_min_tmp[i]
            stack_tmp = [0]
            stack_min_tmp = [0]

        self.stack[self.length] = val
        if self.length > 0:
            self.stack_min[self.length] = val if self.stack_min[self.length-1] > val else self.stack_min[self.length-1]
        else:
            self.stack_min[self.length] = val
        self.length += 1
        
    def pop(self) -> None:
        self.length -= 1
        

    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        return self.stack_min[self.length-1]
        
