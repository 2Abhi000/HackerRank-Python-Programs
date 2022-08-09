#checking arrau is sorted or not using recursion

def issorted_using_recursion(array,index):
    l=len(array)
    if(index==l-1 or index==l):
        return(True)
    if(array[index]>array[index+1]):
        return(False)
    ans=issorted_using_recursion(array,index+1)
    return(ans)
a=[1,2,3,8,5]
ans=issorted_using_recursion(a,0)
print(ans)
