#find index of element(last occurence) using recursion

def findindex(array,no,index):
    l=len(array)
    if(index==l):
        return(-1)
    ans=findindex(array,no,index+1)
    if(ans!=-1):
        return(ans)
    else:
        if(array[index]==no):
            return(index)
        else:
            return(-1)
a=[1,4,5,4,8]
ans=findindex(a,4,0)
print(ans)
        
