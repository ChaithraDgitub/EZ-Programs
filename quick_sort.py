def divide(L,Low,High):
    P=L[High]
    Pi=High
    j=Low-1
    for i in range(Low,High):
        if L[i]<=P:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[Pi]=L[Pi],L[j]
    Pi=j
    return Pi

def Quick_sort(L,Low,High):
    if Low<High:
        Pi=divide(L,Low,High)
        print(Pi,Low,High)
        Quick_sort(L,Low,Pi-1)
        Quick_sort(L,Pi+1,High)
    return

if __name__=="__main__": #not necessary to use main fuction everytime its just for practice
    L=list(map(int,input().split( )))
    Low=0
    High=len(L)-1
    Quick_sort(L,Low,High)
    
    print("sorted array = ",L)