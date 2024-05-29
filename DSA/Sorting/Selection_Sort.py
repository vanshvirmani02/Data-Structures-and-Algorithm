arr=[3,5,4,1,2,9,7]
n=len(arr)
for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[min_index],arr[i]=arr[i],arr[min_index]
print(arr)