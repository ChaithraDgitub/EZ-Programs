Q=[
    [1,2,2,3],
    [3,1,4,2],
    [1,5,3,3],
    [1,2,1,1]
]
sum=Q[0][0]
n=len(Q)
m=len(Q[0])-1
i=j=0
while (i<n-1 or j<m-1):
    if i==n-1:
        j+=1
    elif  j==m-1:
           i+=1
    elif Q[i][j+1]>Q[i+1][j]:
        j=j+1    
    else:
         i=i+1
    sum+=Q[i][j]
print(sum)