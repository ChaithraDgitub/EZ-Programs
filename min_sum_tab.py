Q=[
    [1,2,2,3],
    [3,1,4,2],
    [1,5,3,3],
    [1,2,1,1]
]

for i in range(len(Q[0])-1):
     sum1=(Q[0][i])
     Q[0][i+1]=sum1+Q[0][i+1]
print(Q)        
for i in range(len(Q)-1):
     sum2=Q[i][0]
     Q[i+1][0]=sum2+Q[i+1][0]
print(Q)     
for i in range(len(Q)-1):
     for j in range(len(Q[i])-1):
         a= min(Q[i][j+1],Q[i+1][j])
         Q[i+1][j+1]=Q[i+1][j+1]+a
print(Q)
print(Q[len(Q)-1][len(Q[i])-1])