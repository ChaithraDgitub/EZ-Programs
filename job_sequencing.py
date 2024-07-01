dict={20:2,40:1,10:2,30:3,50:1}
max_deadline=max(dict.values())
p=[20,40,10,30,50]
deadline=[2,1,2,3,1]
d={}
for i in range(len(p)):
    d[p[i]]=deadline[i]
print(d)
m_deadline=max(d.values())
m_p=max(d.keys())
print(m_p)
print(m_deadline)
    