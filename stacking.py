class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)      #for top[-1]
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.items)
print(s.items.pop())
print(s.items)
print(s.size())