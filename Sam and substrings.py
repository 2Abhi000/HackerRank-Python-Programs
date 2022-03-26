#Sam and substrings
a=input()
k=[]
k.append(int(a))
if(len(a)<=2):
    for i in range(len(a)):
        k.append(int(a[i]))
        
else:
    for i in range(len(a)):
        k.append(int(a[i]))
        for j in range(len(a)):
            k.append(int(a[i]+a[j]))

#print(k)
c=0
for i in k:
    if(str(i) in a):
        c=c+int(i)
print(c)
