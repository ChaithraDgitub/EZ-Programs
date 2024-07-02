stack=[]
def push():
    element=int(input())
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(e,"is removed")
        print(stack)
while True:
    '''
    1.To Push
    2.To Pop
    3.Quit
    '''
    choice=int(input())
    match choice:
        case 1:
            push()
        case 2:
            pop()
        case 3:
            break        

            
