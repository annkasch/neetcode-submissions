class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.index_start = 0
        self.index_end = 0
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        self.index_start += 1
        return self.stack1[self.index_start-1]
        

    def peek(self) -> int:
        return self.stack1[self.index_start]
        

    def empty(self) -> bool:
        return len(self.stack1) - self.index_start <= 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()