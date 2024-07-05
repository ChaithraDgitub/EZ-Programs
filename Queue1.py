queue=[]
def enqueue():
    element=input("enter the element :")
    queue.append(element)
    print(element,"is added element")
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:    
        e=queue.pop(0)
        print(e,"is removed from queue")
        print(queue)
while True:
    choice=int(input())
    match choice:
        case 1:
            enqueue()
        case 2:
            dequeue()
        case 3:
            break   