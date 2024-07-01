G=[
    [ 0, 7, -1, -1, -1, -1, -1, 2, -1, -1],
    [ 7, 0, 4, 1, -1, 5, -1, -1, -1, -1],
    [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
    [ -1 ,1 ,-1 ,0 ,6 ,8 ,3 ,3 ,-1 ,-1],
    [ -1 ,-1, -1, 6, 0 ,-1, -1 ,6 ,8 ,-1],
    [ -1 ,5 ,-1 ,8 ,-1 ,0 ,-1 ,-1 ,-1 ,-1],
    [ -1 ,-1, -1, 3 ,-1 , -1, 0 ,-1, 9, 2],
    [ 1 ,-1 ,8 ,3 ,6 ,-1 ,-1 ,0 ,-1 ,-1],
    [ -1 ,-1, -1, -1, 8, -1, 9, -1, 0, -1],
    [ -1 ,-1 ,-1 ,-1 ,-1 ,-1 ,2 ,-1 ,-1 ,0], 
]
temp={}
for i in range(len(G)):
    temp[i]=float('inf')
Dist=[float("inf")]*len(G) 
temp[0]=0   
while len(temp)>0:
    min_value=min(temp.values())
    min_key=min(temp,key=temp.get)
    temp.pop(min_key)
    Dist[min_key]=min_value
    for j in range(len(G[min_key])):
        if G[min_key][j]!=-1 and G[min_key][j]!=0:
            new_dist=min_value + G[min_key][j]
            if j in temp.keys() and temp[j]>new_dist:
                temp[j]=new_dist
print(Dist)      