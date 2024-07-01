a=[20,34,45,70,56,81,104,37,46,39]
l=len(a)+1
res=[0]*l
count=0
for i in a:
    r=i%11
    if res[r]==0:
        res[r]=i
    else:
        count+=1
        r1=8-(i%8)   
        ans=(r+count*r1)%11
        if res[ans]==0:
            res[ans]=i
            count=0
        else:
           count+=1
           ans=(r+count*r1)%11
print(res)