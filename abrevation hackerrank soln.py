#abrevation hackerrank soln
'''a='daBcd'
b='ABC'

a='AbcDE'
b='ABDE'
'''
a='AbfcDE'
b='AFDE'
c=0

cc=[]
for i in b :
    if(i not in a.upper()):
        print("No")
        exit()
else:
    for i in a:
        for j in b:
            if(i==j):
               cc.append(i)
    for i in a:
        if(i.upper() in b and i.upper() not in cc):
            cc.append(i.upper())
k=''

#print(cc,c,k)
if(len(cc)==len(b)):
    
    print("YES")
else:
    print("NO")
