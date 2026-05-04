class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key in self.arr:
            return
        else:
            self.arr.append(key)


    def remove(self, key: int) -> None:
        set_tmp = self.arr
        self.arr = []
        for k in set_tmp:
            if k == key: continue
            self.arr.append(k)


    def contains(self, key: int) -> bool:
        for k in self.arr:
            if k == key:
                return True
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)