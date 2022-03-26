#hackerrank consicutive sub sequence
def solve(array,num):
    c=0
    for i in range(len(array)):
        for j in range(i,len(array)):
            x=int(array[i])+int(array[j])
            if(x%int(num)==0):
                c+=1
    return c
a=[]
n=int(input("Enter the size of array: "))
for i in range(n):
    a.append(int(input()))
k=input("Enter the num: ")
p=solve(a,k)
print(p)
