# Impliment Lower Bound
# TC=O(Log N)
# SC=O(1)

def lower_bound(arr,n,x):
    lb=n
    h=n-1
    l=0
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>=x:
            lb=mid
            h=mid-1
        else:
            l=mid+1
    return lb

arr = [1, 2, 2, 3] 
n=len(arr) 
x = 2
print(lower_bound(arr,n,x))