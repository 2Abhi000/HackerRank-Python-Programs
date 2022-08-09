import heapq
def ksmallest(arr,k):
    heap=arr[:k]
    heapq._heapify_max(heap)
    n=len(arr)
    for i in range(k,n):
        if heap[0]>arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap
a=[10,6,7,2,3,8,9,11,1]
k=4
ele=ksmallest(a,k)
for e in ele:
    print(e,end=" ")
