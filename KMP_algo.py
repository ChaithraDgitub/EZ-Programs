def KMPAlgo(p,s):
    N=len(s)
    M=len(p)
    lps=[]
    LPS(p,M,lps)
    i=0
    j=0
    while (N-i)>=(M-j):
        if p[j]==s[i]:
            i+=1
            j+=1
        if j==M:
            print("pattren found at",i-j)
            j=lps[j-1]
        elif i<N and p[j]!=s[i] :
            if j!=0:
                j=lps[j-1]
            else:
                i+=1           
    print(lps)   

def LPS(p,M,lps):
  l=[0]
  j=0
  p='ABCAB'
  for i in range(1,len(p)):
    if p[i]==p[j]:
        l.append(j+1)
        j=j+1
    else:
        j=0
        l.append(j)
    
s='ABABACDEABABABCABCABCABDAA'
p='ABCAB'
KMPAlgo(p,s)