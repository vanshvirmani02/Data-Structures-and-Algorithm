#Brute Force
arr=[1,2,3,0,0,4,5]
n=len(arr)
temp=[]
count=0
for i in arr:
    if i !=0:
        temp.append(i)
    else:
        count+=1
for j in range(count):
    temp.append(0)
arr[:]=temp
print(arr)

# TC=O(N)+O(K)=O(n+k)
# Sc=O(N)


#Optimal Solution
# TC=O(N)
# SC=O(1)

'''arr=[1,2,3,0,0,4,5]
n=len(arr)
i=0
while i<n-1:
    if arr[i]==0:
        break
    i+=1
j=i+1
while j<n:
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    j+=1
print(arr)'''