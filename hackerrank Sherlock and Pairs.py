#hackerrank Sherlock and Pairs
def solve(a):
    c=0
    for i in range(len(a)):
        for j in range(len(a)):
            if(i!=j and a[i]==a[j]):
                c+=1
    return c

n=int(input("Enter the size of array: "))
s=[]
for i in range(n):
    s.append(int(input()))

print(solve(s))
