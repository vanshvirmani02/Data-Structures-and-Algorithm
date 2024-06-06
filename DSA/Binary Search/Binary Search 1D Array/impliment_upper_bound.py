# Impliment Upper-Bound
# TC=O(Log N)
# SC=O(1)

def upperbound(arr,x,n):
    l=0
    h=n-1
    ub=n
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>x:
            ub=mid
            h=mid-1
        else:
            l=mid+1 
    return ub

arr=[2,4,6,7] 
x=8
n=len(arr)
print(upperbound(arr,x,n))