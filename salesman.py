def cost(curr,visited,g,Dp):
  if len(visited)==n:
    return g[curr][0]
  visit=tuple(visited)
  if (curr,visit) in DP:
    return DP[(curr,visit)]
  m=float('inf')
  for i in range(n):
    if i not in visited:
      new_visit=visited+[i]
      new_cost=g[curr][i]+cost(i,new_visit,g,DP)
      m=min(m,new_cost)
  DP[(curr,visit)] = m
  return m 
g=[
[0,4,7,5,5],
[4,0,2,3,8],
[7,2,0,3,4],
[8,3,3,0,6],
[5,8,4,6,0]
]
n=len(g)
DP={}
print("minimum cost=",cost(0,[0],g,DP))
for i in DP:
  print(i)