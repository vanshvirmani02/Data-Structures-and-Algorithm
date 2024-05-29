def merge(leftarr,rightarr):
    merged = []
    i,j=0,0
    while i < len(leftarr) and j <len(rightarr):
        if leftarr[i]<= rightarr[j]:
            merged.append(leftarr[i])
            i=i+1
        else:
            merged.append(rightarr[j])
            j+=1
    
    while i<len(leftarr):
        merged.append(leftarr[i])
        i+=1
    
    while j<len(rightarr):
        merged.append(rightarr[j])
        j+=1
    return merged


def merge_sort(arr):
    n=len(arr)//2
    if len(arr)<=1:
        return arr
    lefty=arr[:n]
    righty=arr[n:]
    new_lefty=merge_sort(lefty)
    new_righty=merge_sort(righty)
    return merge(new_lefty,new_righty)

arr=[3,1,2,4,1,5,2,6,4]
print(merge_sort(arr))

# Tc= O(N*logN)    log base 2 N
# Sc=O(n)