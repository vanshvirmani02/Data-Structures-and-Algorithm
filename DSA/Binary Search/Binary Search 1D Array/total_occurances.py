# Number of occurances of target in array
#Brute Force
# TC=O(N)
# SC=O(1)

'''arr=[0,1,1,5]
target=4
n=len(arr)
count=0

for i in range(n):
    if arr[i]==target:
        count+=1
print(count)'''
########################################################################################

# Optimal Solution
# TC=O(Log N)
# SC=O(1)

'''def leftist(arr,x,n):
    l=0
    h=n-1
    index=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==x:
            index=mid
            h=mid-1
        elif arr[mid]>x:
            h=mid-1
        else:
            l=mid+1
    return index

def righest(arr,x,n):
    l=0
    h=n-1
    index=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==x:
            index=mid
            l=mid+1
        elif arr[mid]>x:
            h=mid-1
        else:
            l=mid+1
    return index

def firstnlast(arr,k,n):
    first=leftist(arr,k,n)
    last=righest(arr,k,n)
    result=0
    if last != -1:
        result=last-first+1
    else:
        pass
    return result

arr=[0,1,1,5]
n=len(arr)
k=4
print(firstnlast(arr,k,n))
'''
