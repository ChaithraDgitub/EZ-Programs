class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self):
        self.head=None

    def print_linkedlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref        
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node  

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("the value is not present in linked_list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref 
            n.ref=new_node
    def add_before(self,data,x):
        if self.head==None:
            print("list is empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if  n.ref is None:
            print("node is not found in linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node



           
LL1=linked_list()
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_after(40,10)
LL1.add_after(50,70)
LL1.add_before(60,100)
LL1.add_before(90,120)
LL1.print_linkedlist()









 