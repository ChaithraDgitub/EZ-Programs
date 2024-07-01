class Queue:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop(0)
    def size(self):
        return len(self.items)
s=Queue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.items)
s.pop() 
print(s.items)
print(s.size())