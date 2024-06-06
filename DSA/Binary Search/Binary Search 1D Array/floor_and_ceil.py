# Find the Floor and Ceil of a number X
#Floor is the number equal to or just below the target
#Ceiling is the number equal to or just bigger than the target
#TC=O(Log N)
# SC=O(1)

def floor_ceil(arr,x,n):
    l=0
    h=n-1
    floor=-1
    ceil=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==x:
            return x,x
        elif arr[mid]>x:
            ceil=arr[mid]
            h=mid-1
        else:
            floor=arr[mid]
            l=mid+1
    return floor,ceil

x=5
arr=[3, 4, 7, 8, 10]
n=len(arr)
print(floor_ceil(arr,x,n))

