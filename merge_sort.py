def merge(L,low,mid,high):
    left=L[low:mid+1]
    right=L[mid+1:high+1]
    
    i=j=0
    t=low
    
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            L[t]=left[i]
            i+=1
            
        else:
            L[t]=right[j]
            j+=1
        t+=1
            
    while i<len(left):
        L[t]=left[i]
        i+=1
        t+=1
        
    while j<len(right):
        L[t]=right[j]
        j+=1
        t+=1
def merge(L,low,mid,high):
    left=L[low:mid+1]
    right=L[mid+1:high+1]
    
    i=j=0
    t=low
    
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            L[t]=left[i]
            i+=1
            
        else:
            L[t]=right[j]
            j+=1
        t+=1
            
    while i<len(left):
        L[t]=left[i]
        i+=1
        t+=1
        
    while j<len(right):
        L[t]=right[j]
        j+=1
        t+=1

def merge(L,low,mid,high):
    left=L[low:mid+1]
    right=L[mid+1:high+1]
    
    i=j=0
    t=low
    
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            L[t]=left[i]
            i+=1
            
        else:
            L[t]=right[j]
            j+=1
        t+=1
            
    while i<len(left):
        L[t]=left[i]
        i+=1
        t+=1
        
    while j<len(right):
        L[t]=right[j]
        j+=1
        t+=1
def mergesort(L,low,high):
    if low<high:
        mid=(low+high)//2
        mergesort(L,low,mid)
        mergesort(L,mid+1,high)
        
        merge(L,low,mid,high)
    
if __name__=="__main__": 
    L=list(map(int,input().split( )))
    low=0
    high=len(L)-1
    mergesort(L,low,high)
    
    print("sorted array = ",L)    
        
        
        
            