k=[22,10,47,42,56,100,50,92,99]
res=[0]*(len(k)+1)
for i in k:
    hk=i%10
    if res[hk]==False:
        res[hk]=i
    else:
        res[hk+1]=i
print(res)
d=[]
for i in range(len(res)):
    if res[i]!=False:
        d.append(res[i])
print(d)