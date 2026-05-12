class LinkNode:
    def __init__(self, val):
        self.val = val
        self.prev = None

class Queue:
    def __init__(self):
        self.right = None

    def enqueue(self, val):
        newNode = LinkNode(val)
        if self.right: newNode.prev = self.right
        self.right = newNode
    
    def dequeue(self):
        val = self.right.val
        self.right = self.right.prev
        return val

class MyStack:

    def __init__(self):
        self.queue = Queue()
        

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        

    def pop(self) -> int:
        return self.queue.dequeue()
        

    def top(self) -> int:
        return self.queue.right.val
        

    def empty(self) -> bool:
        if not self.queue.right: 
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()