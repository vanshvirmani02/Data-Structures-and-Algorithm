# Search Insert Position ~ Lower Bound
# TC=O(Log N)
# Sc= O(1)

def searchInsert(arr: [int], m: int) -> int:
    n=len(arr)
    l=0
    h=n-1
    ub=n
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>=m:
            ub=mid
            h=mid-1
        else:
            l=mid+1 
    return ub


arr=[1,2,2,4]
m=2
print(searchInsert(arr,m))
