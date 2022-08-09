#find index of element(first occurence) using recursion

def findindex(array,no,index):
    l=len(array)
    if(index==l):
        return(-1)
    if(array[index]==no):
        return(index)
    ans=findindex(array,no,index+1)
    return(ans)
a=[1,2,4,5,6,7,8,9,7]
ans=findindex(a,7,0)
print(ans)
        
