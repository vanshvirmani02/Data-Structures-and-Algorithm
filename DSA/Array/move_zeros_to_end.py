arr=[1,2,0,0,2,3]
i=0
while i < len(arr)-1:
    if arr[i]!=0:
        i+=1
    else:
        j=i+1
        while j < len(arr):
            if arr[j]==0:
                j+=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                break
print(arr)