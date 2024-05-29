arr=[9,3,6,2,0]
n=len(arr)
for i in range(1,n):
    j=i-1
    key=arr[i]
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

print(arr)

# TC=O(n/2+n^2/2)~N^2
# SC=O(1)