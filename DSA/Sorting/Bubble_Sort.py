'''arr=[2,3,1,6,5,4]
n=len(arr)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)'''

#isme hme alag list me save nhi krna padhta kyuki List call by Reference hota hai

# TC = O(N(N+1)/2) ~ O(N**2)
# SC = O(1)


#Optimised tarika but condition is arr should be sorted 

arr=[1,2,5,4,5,6]
def sorted(arr):
    n=len(arr)
    flag=False
    for i in range(n-2):
        if arr[i]>arr[i+1]:
            flag=True
    return flag

print(sorted(arr))

# TC = O(N)
# SC = O(1)
