#Maximum Possible scire
def maximumPossibleScore(N, A):
    ar=[]
    s=0
    for i in range(N):
        an=[]
        for j in range(N):
            an.append(A[i]^A[j])
        ar.append(an)
    for i in ar:
        x=sum(i)
        if(s<x):
            s=x
    return(s)
a=[11,12,13,14,15]
n=len(a)
x=maximumPossibleScore(n,a)
print(x)
