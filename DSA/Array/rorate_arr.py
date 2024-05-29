#Brute Force
# arr = [1, 2, 3, 4, 5]

#Left Rorate an Array for Coding NInjas

'''n=len(arr)

last=arr.pop(0)
arr.insert(n-1,last)
print(arr)'''

#Alternative can be 

'''n=len(arr)

last=arr.pop(0)
arr.append(last)
print(arr)'''
################################################################

#Reverse and Array 

def reverse_Array(arr,start,end):
    num=len(arr)
    i=start
    j=end
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

# arr=[1,2,3,4,5]
# n=len(arr)
# print(reverse_Array(arr,1,n-1))
################################################################



#Better Solution for rotation
'''arr = [1, 2, 3, 4, 5]
k=3
n=len(arr)
r = k%n
arr[:]=arr[n-r:]+arr[:n-r]

print(arr)'''
# TC=O(K)+O(N-K)~O(N)  --> here k is the length of slice array
# SC=O(1)

################################################################

#Optimal Solution

arr=[1,2,3,4,5]
k=2
n=len(arr)
r = k % n

reverse_Array(arr,0,r-1)
reverse_Array(arr,r,n-1)
reverse_Array(arr,0,n-1)
print(arr)